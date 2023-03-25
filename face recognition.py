import os
import cv2
import picamera
import picamera.array
import numpy as np
import pyttsx
import RPi.GPIO as gpio
from time import sleep

import pyttsx
rate = 140
sayit=pyttsx.init()
sayit.setProperty('voice','english-un')


sayit.setProperty('rate',rate)

gpio.cleanup()
gpio.setmode(gpio.BOARD)
pin = 7

gpio.setup(pin,gpio.OUT)
labels=[]
names=[]
f= open('/home/pi/Documents/faces/labels','r')
y=f.readlines()
y = [x.strip() for x in y]
lenght = len(y)
for i in range(1,lenght):
    x=y[i].split('-')
    labels.append(x[0])
    names.append(x[1])
f.close()
def detect_me():
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    return haar_face_cascade
def understand_me():
    reader = cv2.createLBPHFaceRecognizer()
    reader.load('trainedset.yml')
    return reader

def recognize_me(read,detecter):
    read=reader
    haar_face_cascade=detecter

    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution = (320, 240)

            while True:
                camera.capture(stream, 'bgr', use_video_port=True)
                

                
                cv2.imshow('Frame',stream.array)
                gray_img=cv2.cvtColor(stream.array,cv2.COLOR_BGR2GRAY)
               
                detected = haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
                for(x,y,w,h) in detected:
                    hello=0  
                
                if len(detected )>0:
                    cropimg=gray_img[y-10:y+h+10,x-10:x+w+10]
                    
                    ids,unknown = reader.predict(cropimg)


                    p='s'+str(ids)

                   
                    if unknown<70:
                        for i in range(len(labels)):
                            if ids==1:
                                gpio.output(pin,1)
                            else:
                                gpio.output(pin,0)
                            if labels[i]==p:
                                display ='hey'+','+names[i]
                                print display
                                sayit.say(display)
                                sayit.runAndWait()
                                print unknown
                    else:
                        gpio.output(pin,0)
                        print"unknown face"
                        sayit.say("can not recognize your face")
                        sayit.runAndWait()
                        print unknown
                    


                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # reset the stream before the next capture
                stream.seek(0)
                stream.truncate()

            cv2.destroyAllWindows()
detecter= detect_me()
reader=understand_me()
recognize_me(reader,detecter)
