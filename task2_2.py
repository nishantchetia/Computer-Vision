import cv2
n = int(input(print("Save a frame after how many frames?")))
cap= cv2.VideoCapture(0)
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if count%n == 0:
        cv2.imwrite('IMG_' + str(count)+'.jpg',frame)
        continue
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
