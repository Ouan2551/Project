# Thresholding => assignment pixel values in relation to the threshold value provided
# main core => if pixel value smaller than threshold it set to 0 but another
# it set to 255 (work on grayscale image)
# thresholding popular segmentation technic use separating object consider
# foreground from it background

# logic
# If f (x, y) < T 
#    then f (x, y) = 0 
# else 
#    f (x, y) = 255

# where 
# f (x, y) = Coordinate Pixel Value
# T = Threshold Value.

# Simple Thresholding
import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply different thresholding (all pixel value above 120 will set to 255)
ret, thresh1 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_TOZERO_INV)

# showing output image
cv2.imshow('Binary Threshold', thresh1) 
cv2.imshow('Binary Threshold Inverted', thresh2) 
cv2.imshow('Truncated Threshold', thresh3) 
cv2.imshow('Set to 0', thresh4) 
cv2.imshow('Set to 0 Inverted', thresh5) 

cv2.waitKey(0)
cv2.destroyAllWindows()