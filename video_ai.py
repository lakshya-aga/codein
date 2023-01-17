import csv
import numpy as np
import tensorflow as tf 
from tensorflow.keras.utils import to_categorical
import datetime
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Activation , Dropout ,Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.metrics import categorical_accuracy
from tensorflow.keras.models import model_from_json
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import *
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import cv2

#change path to data
model = model_from_json(open('/kaggle/input/tf-model/fer.json', 'r').read())
model.load_weights('/kaggle/input/tf-model/fer.h5')


face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
def OccurEmot(input_emot):
    global data
    timestamps=[]
    for i in range(len(data)):
        if(input_emot==data[i][1]):
            timestamps.append(data[i][0])
    return [timestamps, len(timestamps)]

def analyse_video(video_path):

    window_name = f"Detected Objects in {video_path}"
    cap = cv2.VideoCapture(video_path)
    img_counter = 0

    counter=[0,0,0,0,0,0,0]
    while True:
        check, img = cap.read()
        if not check:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscale for model
    
        faces = face_cascade.detectMultiScale(gray,1.3,3)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,100,50), 4) # drawing rectangle of colour blue
            roi_gray=gray[y:y+w,x:x+h] # cropping region of interest i.e. face area from  image
            roi_gray=cv2.resize(roi_gray,(48,48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis = 0)
            img_pixels /= 255 # converting to model compliant data form
        
        
            predictions = model.predict(img_pixels) # pass ROI through model
            
            #find max indexed array
            max_index = np.argmax(predictions[0])
        
            emotions = ('Angry','Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral') # tuple of emotions
            predicted_emotion = emotions[max_index]
            counter[max_index] = counter[max_index]+1

            cv2.putText(img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2) # formatting emotion text
        

        resized_img = cv2.resize(img, (1000,700)) # resizing window
        #cv2.imshow('Face', resized_img)
        #key = cv2.waitKey(10)
        #if key == ord('q'): # enabling hotkey to exit program
        #break
        #elif key%256 == 32: 
        # SPACE pressed
    #         img_name = "{}_frame{}.png".format(predicted_emotion,img_counter)
#         cv2.imwrite(img_name, img)
#         print("{} written!".format(img_name))
#         img_counter += 1

        cap.release()
#cv2.destroyAllWindows()

    negative = counter[0]+counter[1]+counter[2]+counter[4]+counter[5]
    neutral = counter[6]
    positive = counter[3]
    return negative,positive,neutral

import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

#load any audio file of your choice
def speech_analysis(video_path):
    speech, rate = librosa.load(video_path,sr=16000)
    input_values = tokenizer(speech, return_tensors = 'pt').input_values

    logits = model(input_values).logits

    #Store predicted id's
    predicted_ids = torch.argmax(logits, dim =-1)

    transcriptions = tokenizer.decode(predicted_ids[0])
    #print(transcriptions)

    from transformers import pipeline
    senti_pipeline = pipeline('sentiment-analysis')
    return senti_pipeline(transcriptions)