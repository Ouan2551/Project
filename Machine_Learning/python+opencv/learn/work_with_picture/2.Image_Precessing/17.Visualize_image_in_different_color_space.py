import cv2
import matplotlib.pyplot as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"

# RGB image
image = cv2.imread(path)
plt.imshow(image)
plt.waitforbuttonpress()

# YCrCb color space
image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("image_YCrCb : ", image_YCrCb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# HSV color space
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("image_HSV : ", image_HSV)
cv2.waitKey(0)
cv2.destroyAllWindows()

# LAB color space
image_LAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("image_LAB : ", image_LAB)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Edge map of image
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('EdgeMap', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Hest map of image
plt.imshow(image, cmap='hot')

#Spectral Image map
plt.imshow(image, cmap='nipy_spectral')