import sys
import os

# --- PYINSTALLER WINDOWED FIX ---
# This creates a "black hole" for any print statements so they don't crash the app
class NullWriter:
    def write(self, text): pass
    def flush(self): pass

if sys.stdout is None: sys.stdout = NullWriter()
if sys.stderr is None: sys.stderr = NullWriter()

# Silence TensorFlow terminal warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# --------------------------------

import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf

# 1. Setup the Main Application Window
root = tk.Tk()
root.title("Neurological MRI Analyzer")
root.geometry("600x700")
root.configure(bg="#f0f4f8")

# 2. Load the AI Brain
model_path = 'brain_tumor_v4_PRO.keras'
try:
    model = tf.keras.models.load_model(model_path)
    class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
except Exception as e:
    messagebox.showerror("Error", f"Could not load the AI model.\nMake sure '{model_path}' is in the same folder as this app.\nError: {e}")
    root.destroy()

# 3. The Core Diagnostic Function
def analyze_image():
    file_path = filedialog.askopenfilename(
        title="Select an MRI Scan",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    
    if not file_path:
        return 
        
    try:
        # Display the image
        display_img = Image.open(file_path).resize((300, 300))
        img_tk = ImageTk.PhotoImage(display_img)
        image_label.configure(image=img_tk)
        image_label.image = img_tk
        
        # Prepare the image
        ai_img = tf.keras.utils.load_img(file_path, target_size=(224, 224), color_mode="grayscale")
        img_array = tf.keras.utils.img_to_array(ai_img) / 255.0
        img_array = tf.expand_dims(img_array, 0)
        
        # Ask the AI
        result_label.config(text="Analyzing...", fg="blue")
        root.update()
        
        # verbose=0 is the magic key here!
        predictions = model.predict(img_array, verbose=0)
        confidence = np.max(predictions[0]) * 100
        predicted_index = np.argmax(predictions[0])
        diagnosis = class_names[predicted_index]
        
        # Update the UI
        if diagnosis == "No Tumor":
            color = "green"
        else:
            color = "red"
            
        result_label.config(text=f"Diagnosis: {diagnosis}\nConfidence: {confidence:.2f}%", fg=color)
        
    except Exception as e:
        messagebox.showerror("Processing Error", f"An error occurred while analyzing the image:\n{e}")

# 4. Build the UI Elements
title_label = tk.Label(root, text="Neurological MRI Analyzer", font=("Helvetica", 20, "bold"), bg="#f0f4f8", pady=20)
title_label.pack()

upload_btn = tk.Button(root, text="Upload Patient MRI", font=("Helvetica", 14), bg="#007acc", fg="white", padx=20, pady=10, command=analyze_image)
upload_btn.pack(pady=20)

image_label = tk.Label(root, bg="#f0f4f8")
image_label.pack(pady=20)

result_label = tk.Label(root, text="Awaiting Scan...", font=("Helvetica", 18, "bold"), bg="#f0f4f8")
result_label.pack(pady=20)

# 5. Start the Application
root.mainloop()