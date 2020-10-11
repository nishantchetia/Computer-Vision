import cv2
import numpy as np     # To staqck the frames horizontally

video = cv2.VideoCapture(0)
x = 0
while True:
    x = x+1
    ret, frame= video.read()



    # Fliping the image as said in question
    vid_flip = cv2.flip(frame,0)

    # Combining the two different image frames in one window
    combined_window = np.hstack([frame,vid_flip])

    # Displaying the single window
    cv2.imshow("Combined videos ",combined_window)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print(x)

video.release()
cv2.destroyAllWindows
