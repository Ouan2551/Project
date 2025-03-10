import matplotlib.pyplot as plt
import cv2
# Histogram => graph show frequency pixel  range from 0 to 255 (gray scale image)
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create from image use numpy array
plt.hist(image_gray.ravel(), bins = 256, range = (0.0, 1.0), fc = 'k', ec = 'k')
plt.show()

# calculate frequency pixel in range 0-255
histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.show()

# alternative way to find histogram image
plt.hist(image_gray.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("original image : ", image)
cv2.waitKey(0)