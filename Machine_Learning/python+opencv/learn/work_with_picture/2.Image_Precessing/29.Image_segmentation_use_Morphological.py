# extract or define something from image
import numpy as np
import cv2
import matplotlib.pyplot as plt


path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\coin-detection.jpg'
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# normal have some noise
ret, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow("image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# remove all white noise (use morphological closing to remove it)
# closing operation
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# background area use dilation
bg = cv2.dilate(closing, kernel, iterations=1)

# finding foreground area
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
ret, fg = cv2.threshold(dist_transform, 0.02 * dist_transform.max(), 255, 0) 

cv2.imshow('image', fg) 
cv2.waitKey(0)
cv2.destroyAllWindows()