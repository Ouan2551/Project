# open-cv => open source computer vision library

# 1) Reading image
# import open cv library
import cv2
# reading image use "imread()" in this case i use full location file for make sure nothing wrong
image = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\image.jpg")

# extract height and width of image
h, w = image.shape[:2]

# display height and width
print("Height = {}, Width = {}".format(h,w))

# 2) Extracting the RGB Values of a Pixel
# passing with 100, 100 height and weight
(R, G, B) = image[100, 100]

# display pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# display specific values
# structure image[width, height, 0 = R | 1 = G | 2 = B]
B_value = image[100, 100, 2]
print("B_value = {}".format(B_value))

# 3) Extracting the Region of Interest (ROI)
# output some part of picture
roi = image[200:1100, 200:700]
cv2.imshow("ROI : ", roi)
cv2.waitKey(0) # this line do wait program until you close

# 4) Resizing the Image
resize = cv2.resize(image, (500,500))
cv2.imshow("Resized Image : ", resize)
cv2.waitKey(0)

# problem is it chance aspect ratio
# calculate ratio
ratio = 800/w

# create tuple contain width and height
# tuple is data type can store multiple type (can't change value)
dim = (800, int(h*ratio))

# resize image
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image : ", resize_aspect)
cv2.waitKey(0)