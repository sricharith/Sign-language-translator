# 🤟 Sign Talk: Real-Time ASL Translator

**Sign Talk** is an end-to-end Computer Vision solution designed to bridge the communication gap for the hearing and speech impaired. By leveraging the power of **YOLOv11** and **OpenCV**, this application detects American Sign Language (ASL) gestures via webcam and translates them into text and speech in real-time.

### 📜 Project report doument Link : [Google Drive](https://drive.google.com/file/d/1u0a-EsmzTmI1Y3fpYHU70sDv4sgtqY9Z/view?usp=sharing)

---

## 🚀 Features
* **Real-Time Detection:** High-speed gesture recognition using the latest YOLOv11 architecture.
* **Large-Scale Training:** Trained on a robust dataset of ~3,000 images.
* **Speech Integration:** Built-in translation and text-to-speech capabilities.
* **Easy Deployment:** One-click launch files for Jupyter and Webcam modules.



## 🛠️ Technical Stack
* **Model:** YOLOv11 (Ultralytics)
* **Language:** Python
* **Libraries:** OpenCV, TensorFlow, Scikit-learn, Googletrans, Playsound
* **Environment:** Jupyter Notebook
* **Hardware:** Optimized for iPad Air (M1) and PC environments.



## ⚙️ Installation & Setup

### 1. Clone the Repository
git clone [https://github.com/sricharith/Sign-language-translator.git](https://github.com/sricharith/Sign-language-translator)
cd sign-talk

pip install ultralytics scikit-learn tensorflow opencv-python
pip install googletrans==4.0.0-rc1 playsound==1.2.2

## 🖥️ How to Run
Follow this specific sequence to ensure the system initializes correctly:

1.Training: Open runJupyter.bat and run the YOLO_training.ipynb notebook to train the model.

2.Detection Check: Run SignDetection.ipynb to verify the model is picking up signs correctly.

3.Launch Application: Run the main.py file or double-click runCam.bat.

4.Interaction: * The webcam window will open.

5.Select hand sign from webcam and display a gesture.

6.The system will detect and translate the sign instantly.

7.Exit: Press 'Q' on your keyboard to close the application.

## 📊 Dataset Information
The model was trained using a comprehensive dataset of 3,000+ images, split into:

Training Set: Used to teach the model various hand gestures.

Validation Set: Used to verify accuracy and generalization.

YAML Config: Includes directory paths for seamless integration into the training pipeline.
