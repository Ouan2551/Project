# use for noise removal, smoother image, low intensity edges get remove
# blur some object not want to show e.g. blur plate car number
# type of blur
# 1) Gaussian blur => reduce image noise and detail also process
# before machine learning or deep learning
# 2) Median blur => remove  noise from image or signal
# 3) Bilateral blur => replace intensity of pixel with weight
# of average intensity nearly pixel

import cv2
import numpy as np
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
window_name = "image"

# original
cv2.imshow("Original : ", image)
cv2.waitKey(0)

# Gaussian blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gaussian Blur : ", Gaussian)
cv2.waitKey(0)