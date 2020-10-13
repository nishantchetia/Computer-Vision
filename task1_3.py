import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

count = 0
flipped = False
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
       if not flipped:
           cv2.imshow('frame', gray)
           if count % 5 == 0:
               flipped = True
       elif flipped:
           gray = cv2.flip(gray, 0)
           cv2.imshow('frame', gray)
           if count % 5 == 0:
               flipped = False
       count += 1
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
