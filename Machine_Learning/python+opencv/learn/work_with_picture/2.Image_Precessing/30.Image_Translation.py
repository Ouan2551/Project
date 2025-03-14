# e.g. image form one location to another
import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

height, width = image.shape[:2]
quarter_height, quarter_width = height/4, width/4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# We use warpAffine to transform 
# the image using the matrix, T 
img_translation = cv2.warpAffine(image, T, (width, height)) 

cv2.imshow("Original_image", image) 
cv2.imshow('Translation', img_translation) 
cv2.waitKey() 

cv2.destroyAllWindows() 