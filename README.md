# TKR
Introduction: Computer vision library, developed by intel

Numpy: Numerical analysis

Installation: Requires VS C++ build tools and install directly through preferred IDE

$ pip install opencv-python

Test OpenCV Installation

C:\$ python

 import cv2
 
 print(cv2.__version__)
 
'4.0.0'

pip is a package management system used to install and manage software packages written in Python

OpenCV is an image processing library created by Intel and later supported by Willow Garage and now maintained by Itseez. opencv is available on Mac, Windows, Linux. Works in C, C++, and Python.

it is Open Source and free. opencv is easy to use and install.

Sample images available at https://github.com/opencv/opencv/tree/master/samples/data

cv2.imshow('image', img) to show an image in a window, 

 cv2.waitKey(0) to wait for a key event,
 
 cv2.destroyAllWindows() to destroy all windows, 
 
 cv2.imwrite('lena_copy.png', img) to write images to file.

Read an image

cv2.imread() Second argument is a flag which specifies the way image should be read.'

flag  integer value  description

cv2.IMREAD_COLOR  1  Loads a color image.

cv2.IMREAD_GRAYSCALE  0  Loads image in grayscale mode

cv2.IMREAD_UNCHANGED  -1  Loads image as such including alpha channel

https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d for video capture properties

Python: cv.CAP_PROP_FRAME_WIDTH: Width of the frames in the video stream.

Python: cv.CAP_PROP_FRAME_HEIGHT: Height of the frames in the video stream. 

Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. 
