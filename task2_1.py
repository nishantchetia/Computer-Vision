import numpy as np
import cv2
cap = cv2.VideoCapture(0)

h=w=int(input("enter side of square"))
x=y= 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
count = 0
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        crop_frame = frame[y:y + h, x:x + w]


        if count%2 !=0:
            cv2.imshow('frame', crop_frame)
        else:
            crop_frame = cv2.flip(crop_frame, 0)
            cv2.imshow('frame', crop_frame)
        count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
