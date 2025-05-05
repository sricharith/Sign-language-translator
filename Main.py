#window based webcam coding
from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from ultralytics import YOLO
import cv2
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import os
import time

sign_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z', 'Apple', 'Can', 'Get', 'Good', 'Give me a call', 'I love you', 'I want money', 'I want to go to the washroom', 
               'Please stop', 'Thank you very much']

#yolo confidence threshold to detect hand signs
CONFIDENCE_THRESHOLD = 0.50
GREEN = (0, 255, 0)
yolo_model = YOLO("model/yolo11_best.pt")
print("Yolo11 Model Loaded")
language_type = "English"
translator = Translator()

def language():
    global language_type
    language_type = "Hindi"

def texttospeech(text, filename):
    global language_type
    filename = filename + '.mp3'
    code = "en"
    if language_type == "Hindi":
        code = "hi"
    if os.path.exists(filename):
        os.remove(filename)
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang=code, slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return
    

#function to detect signs using YOLO11
def detectSign(frame):
    global yolo_model, sign_labels
    detections = yolo_model(frame)[0]
    label = "unknown"
    # loop over the detections
    for data in detections.boxes.data.tolist():
        print(data)
        # extract the confidence (i.e., probability) associated with the detection
        confidence = data[4]
        cls_id = data[5]
        # filter out weak detections by ensuring the 
        # confidence is greater than the minimum confidence
        if float(confidence) >= CONFIDENCE_THRESHOLD:
            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            label = sign_labels[int(cls_id)]
            cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), GREEN, 2)
            cv2.putText(frame, sign_labels[int(cls_id)], (xmin, ymin-10),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 0, 0), 2)            
    return frame, label

#in above screen defining function to detect sign and gesture from webcan
def signfromWebcam():
    global model, sc, min_detection_confidence, min_tracking_confidence, labels
    camera = cv2.VideoCapture(0)
    while(True):
        (grabbed, frame) = camera.read()
        if frame is not None:
            frame, label = detectSign(frame.copy())#call yolo to get sign
            cv2.imshow("Sign Langauge Prediction", frame)
            keypress = cv2.waitKey(1) & 0xFF
            if keypress == ord("q"):
                break
            if label != "unknown":
                if language_type == "Hindi":
                    text_to_translate = translator.translate(label, src="en", dest="hi")
                    label = text_to_translate.text
                texttospeech(label, "voice")
                time.sleep(1)
        else:
            break
    camera.release()
    cv2.destroyAllWindows()

main = tkinter.Tk()
main.title("Sign Language Detection")
main.geometry("600x300")

font = ('times', 16, 'bold')
title = Label(main, text='Sign Language Detection')
title.config(bg='chocolate', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')

HindiButton = Button(main, text="Speak Sign in Hindi", command=language)
HindiButton.place(x=200,y=100)
HindiButton.config(font=font1)

camButton = Button(main, text="Hand Sign from Webcam", command=signfromWebcam)
camButton.place(x=200,y=150)
camButton.config(font=font1)  
main.config(bg='light salmon')
main.mainloop()    
