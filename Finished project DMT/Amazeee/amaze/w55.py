import cv2
import os
import webbrowser
import time
gmail="www.gmail.com"
youtube="www.youtube.com"

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
def check_face():
    
    while 1:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print("No of faces found:",len(faces))
        if(len(faces)>0):
            webbrowser.open_new(youtube)
            break
        else:
            shutdown=input("you want to shut down")
            if(shutdown=='yes'):
              os.system('shutdown --s')
              break
            else:
                print("shutdown aborted")
                break
        cap.release()
        cv2.destroyAllWindows()
check_face()
time.sleep(15)
check_face()
    












