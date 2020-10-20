import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
n = int(input(print("Enter the number of frames after which flip needed:")))
count = 0
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)

        if count%n != 0:
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
