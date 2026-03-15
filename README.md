# Neurological MRI Analyzer (v1.0-beta) 🧠✨

A standalone Windows application that utilizes a **Deep Learning Convolutional Neural Network (CNN)** to classify brain tumors from MRI scans.

## 🚀 The Journey: Evolution of the Model
This project tracks the iterative development of a medical imaging AI, moving from basic classification to a robust, "Tough Love" training pipeline.

| Version | Key Features | Performance | Result |
| :--- | :--- | :--- | :--- |
| **V1/V2** | Basic CNN, Standard Dataset | ~60% Accuracy | High Overfitting |
| **V3** | Dropout Layers + Improved Architecture | ~85% Accuracy | Better Generalization |
| **V4 PRO**| **Data Augmentation + Early Stopping + Sniper LR** | **91% Val Accuracy** | **Clinical Grade Logic** |

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Framework:** TensorFlow / Keras
* **UI:** Tkinter (Custom Dark/Clinical Theme)
* **Deployment:** PyInstaller (Standalone Windows .exe)

## 🔍 Current Engineering Focus: Addressing Data Bias
While V4 shows high accuracy, internal testing revealed a "Background Bias" where the model relied on image cropping rather than pure anatomy.
**Next Steps:**
- [ ] Implementing **5-Fold Cross-Validation** to ensure mathematical stability.
- [ ] Integrating the **BraTS Dataset** for multi-institutional diversity.
- [ ] Refining the preprocessing pipeline to eliminate background noise.


> **Disclaimer:** This project is for educational and research purposes only. It is not intended for clinical use or medical diagnosis.
