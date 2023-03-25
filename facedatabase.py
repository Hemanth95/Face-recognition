import cv2
import picamera
import os
import picamera.array
j=0
folderloc = raw_input("folder name   :--")
name= raw_input('name   :--')
path = os.path.join('/home/pi/Documents/faces',folderloc)
if not os.path.exists(path):
    os.makedirs(path)

f= open('/home/pi/Documents/faces/labels','a')
f.write('\n'+folderloc+'-'+name)
f.close()


with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            

            
            
            gray_img=cv2.cvtColor(stream.array,cv2.COLOR_BGR2GRAY)
            haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            detected = haar_face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)

            for(x,y,w,h) in detected:
                hello=0           
            cv2.imshow("Frame", stream.array)
            if len(detected)>0:
                face = 'img'+str(j)
                print 'iam here'
                cropimg=stream.array[y-10:y+h+10,x-10:x+w+10]
                cv2.imwrite(os.path.join(path,face+'.jpg'),cropimg)
                j=j+1;


            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # reset the stream before the next capture
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()
        
                                 
        



