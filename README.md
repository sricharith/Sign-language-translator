# 🤟 Sign Talk: Real-Time ASL Translator

**Sign Talk** is an end-to-end Computer Vision solution designed to bridge the communication gap for the hearing and speech impaired. By leveraging the power of **YOLOv11** and **OpenCV**, this application detects American Sign Language (ASL) gestures via webcam and translates them into text and speech in real-time.

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



## 📂 Project Structure
```text
├── Data/
│   ├── images/ (Train & Validation)
│   └── labels/ (YOLO format annotations)
├── Model/          # Saved weights (.pt or .h5 files)
├── dataset.yaml    # Path configuration for training
├── YOLO_training.ipynb     # Step 1: Model training logic
├── SignDetection.ipynb      # Step 2: Detection testing
├── main.py         # Core application logic
├── runCam.bat      # Quick-start webcam script
└── runJupyter.bat  # Quick-start notebook server


