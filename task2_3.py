import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

count = 0
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:


        if count%5000 != 0:
            cv2.imshow('frame', frame)
        else:
            frame = cv2.flip(frame,0)
            cv2.imshow('frame', frame)

        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
