# Otsu_thresholding -> isn't chosen like another thresholding but it considered

import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply Otsu thresholding
ret, thresh1 = cv2.threshold(image_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# output image
cv2.imshow("Original_image", image)
cv2.imshow("Gray", image_gray)
cv2.imshow("Otsu", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()