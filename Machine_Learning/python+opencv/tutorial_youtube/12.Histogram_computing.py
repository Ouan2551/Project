import cv2
import matplotlib.pyplot as plt
import numpy as np

# histogram (gray scale) => victual picture intensity
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cats.jpg'
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image', gray_image)

# 1) Gray scale histogram
gray_histogram = cv2.calcHist(images=[gray_image], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.title("gray_scale_histogram1")
plt.xlabel("Bins")
plt.ylabel("intensity of pixels")
plt.plot(gray_histogram)
plt.xlim([0,256])
plt.show()

# 2) use with mask (gray scale)
# mask zone
blank = np.zeros(shape=image.shape[:2], dtype='uint8')
rectangle = cv2.rectangle(blank, pt1=(100, 100), pt2=(400,400), color=255, thickness=-1)
mask_image = cv2.bitwise_and(image, image, mask=rectangle)
cv2.imshow("mask_image", mask_image)
# histogram zone
gray_histogram = cv2.calcHist(images=[gray_image], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.title("gray_scale_histogram2")
plt.xlabel("Bins")
plt.ylabel("intensity of pixels")
plt.plot(gray_histogram)
plt.xlim([0,256])
plt.show()

# 3) histogram (color)
plt.figure()
plt.title("Colors_histogram")
plt.xlabel("Bins")
plt.ylabel("intensity of pixels")
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histogram = cv2.calcHist(images=[image], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(histogram, color=col)
    plt.xlim([0,256])
plt.show()

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()