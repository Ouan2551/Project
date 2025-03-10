import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create histogram equalization
equalization = cv2.equalizeHist(image)

# stack image side by side
res = np.hstack((image_gray, equalization))

# show image input compare with output
cv2.imshow("Image : ", res)

cv2.waitKey(0)
cv2.destroyAllWindows()