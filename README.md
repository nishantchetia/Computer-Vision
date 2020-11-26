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

cv2.line() : Used to draw line on an image.

cv2.rectangle() : Used to draw rectangle on an image.

cv2.circle() : Used to draw circle on an image.

cv2.putText() : Used to write text on image.

Capturing mouse click events with Python and OpenCV is easy. we just need to create a callback function and call  this callback function using cv2.setMouseCallback('image', click_event_callback_function) method


OpenCV supports for detecting of mouse events. These Mouse events include mouse clicks (like  left-button down, left-button up, left-button double-click etc) and movements over an attached OpenCV window. Capturing mouse click events with Python and OpenCV is easy. we just need to create a callback function and call  this callback function using cv2.setMouseCallback('image', click_event_callback_function) method

img.shape returns a tuple of number of rows, columns, and channels

img.size returns Total number of pixels is accessed

img.dtype returns Image datatype is obtained

cv2.split(img) - output vector of arrays; the arrays themselves are reallocated, if needed.

cv2.merge((b,g,r)) - The number of channels will be the total number of channels in the matrix array.


cv2.resize - resize the image


dst = cv2.add(img, img2) - Calculates the per-element sum of two arrays or an array and a scalar.


dst = cv2.addWeighted(img, .2, img2, .8, 0) - Calculates the weighted sum of two arrays.


Bitwise operations likebitwise_and(), bitwise_or(), bitwise_xor(), and bitwise_not() are useful when working with masks


Trackbar as the Color Palette and changing colored image to grayscale image using Trackbar switch. We can also get get user input with OpenCV trackbars.


 Implementing color and shape-based object detection and tracking using  hue-saturation-value (HSV) color model. For Choosing the correct upper and lower HSV boundaries for color detection with`cv::inRange` (OpenCV) we will use trackbar.


Simple Image Thresholding is used for image segmentation. Thresholding is the simplest method of image segmentation. From a grayscale image, thresholding can be used to create binary images.

In Thresholding we Pick a threshold T.

1.Pixels above threshold get new intensity A.

2.Pixels above threshold get new intensity B.  

In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.


Adaptive Thresholding algorithm provide the image in which Threshold values vary over the image as a  function of  local image characteristics. So Adaptive Thresholding involves two following steps

(i) Divide image into strips 

(ii) Apply global threshold method to each strip.



So in Adaptive Thresholding, Threshold depends on both f(x,y) and p(x,y). Adaptive thresholding changes the threshold dynamically over the image. Adaptive thresholding typically takes a gray scale or color image as input and, in the simplest implementation, outputs a binary image representing the segmentation.


matplotlib is a User friendly, but powerful, plotting library for python. I is commonly used with OpenCv images. pylab is a module in matplotlib that gets installed alongside matplotlib; and matplotlib.pyplot is a module in matplotlib. matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats.


different functions like : cv.erode(), cv.dilate(), cv.morphologyEx() etc.


different morphological operations like 2D Convolution ( Image Filtering ) and  Image Blurring (Image Smoothing) using Averaging, Gaussian Blurring, Median Blurring, Bilateral Filtering etc. We will see different functions like : cv.filter2D(), cv.blur(), cv.GaussianBlur(), cv.medianBlur(), cv.bilateralFilter() etc.


Image Gradients and Edge Detection with OpenCV. OpenCV provides three types of gradient methods or High-pass filters, Sobel, Scharr and Laplacian.

OpenCV provides method called Canny for Canny edge detector

The Canny edge detection algorithm is broken down to 5 steps:


Noise reduction;

Gradient calculation;

Non-maximum suppression;

Double threshold;

Edge Tracking by Hysteresis.


There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids

Gaussian pyramids use cv.pyrDown() and cv.pyrUp() functions.


cv2.findContours(), cv2.drawContours().

These function retrieves contours from the binary image. The contours are a useful tool for shape analysis and object detection and recognition. 


Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose.


