# Adaptive_Thresholding => this method threshold value calculated for small regions
# (different another because it help in case different lighting area)

import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply different thresholding
thresh1 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5) 

thresh2 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                cv2.THRESH_BINARY, 199, 5)

# show output image
cv2.imshow("Mean", thresh1)
cv2.imshow("Gaussian", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()