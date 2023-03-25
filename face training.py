import os
import cv2
import picamera
import picamera.array
import numpy as np

def setdata(path):

    images=[]
    labels=[]

    folders = os.listdir(path)
    for i in range(len(folders)):
        num=0
        fpath=os.path.join(path,folders[i])
        p=os.path.basename(fpath)
        if p!='labels':
            for i in range(1,len(p)):
                num=int(str(num)+str(p[i]))
        
            for i in range(30):
                if os.path.exists(os.path.join(fpath,'img'+str(i)+'.jpg')):
                    img= cv2.imread(os.path.join(fpath,'img'+str(i)+'.jpg'))
                    
                    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           
            
            
                    images.append(gray_img)
                    labels.append(num)
    
    
    return images,labels


path='/home/pi/Documents/faces'
faces,names = setdata(path)


print names
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.train(faces,np.array(names))
recognizer.save('trainedset.yml')
print "trained"


