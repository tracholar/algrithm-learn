import cv2
import numpy as np


cap = cv2.VideoCapture('fdtd1d.avi')
while(True):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        
    
cap.release()
cv2.destroyAllWindows()