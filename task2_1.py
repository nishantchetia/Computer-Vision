import numpy as np
import cv2
cap = cv2.VideoCapture(0)

w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)
x,y,h,w = 0,0,25,25

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('result.avi', fourcc, fps, (w, h))

flipped = False
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        crop_frame = frame[y:y + h, x:x + w]
    

        if not flipped:
            cv2.imshow('frame', crop_frame)
            flipped = True
        elif flipped:
            crop_frame = cv2.flip(crop_frame, 0)
            cv2.imshow('frame', crop_frame)
            flipped = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
