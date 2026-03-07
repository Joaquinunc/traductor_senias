import cv2

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret, im=cap.read()
    
    if ret == False:
        break
        
        
    cv2.imshow('imagen',im)
    
    if cv2.waitKey(1) == 27:
        break
