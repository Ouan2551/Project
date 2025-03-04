# open-cv => open source computer vision library

# import open cv library
import cv2
# reading image use "imread()"
image = cv2.imread('image.jpg')

# extract height and width of image
h, w = image.shape[:2]

# display height and width
print("Height = {}, Width = {}".format(h,w))