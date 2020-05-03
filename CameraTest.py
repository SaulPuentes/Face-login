from datetime import datetime
import numpy as np

import cv2


faceCascade = cv2.CascadeClassifier('./resources/Cascades/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(50, 50)
    )
    
    for (x,y,w,h) in faces:
        path = "dataset/User." + str(datetime.now()) + ".jpg"
        cv2.imwrite(path, frame[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        print("[INFO] x:{}, y:{}, w:{}, h:{}".format(x,y,w,h))
    
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
