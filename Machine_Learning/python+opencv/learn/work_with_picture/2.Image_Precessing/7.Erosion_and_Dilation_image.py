# erosion => erode away  boundaries the foreground object
# dilation => noise remove, 
import cv2
import numpy as np
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

# take matrix size 5 as kernel
kernel = np.ones((5, 5,), np.uint8)

image_erosion = cv2.erode(image, kernel, iterations=1)
image_dilation = cv2.dilate(image, kernel, iterations=1)

cv2.imshow("Image Original : ", image)
cv2.imshow("Erosion : ", image_erosion)
cv2.imshow("Dilation : ", image_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()