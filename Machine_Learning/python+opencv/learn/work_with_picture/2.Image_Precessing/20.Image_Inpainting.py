# remove damage like noise strokes or text on image
# useful for restore old photograph
# by doing this instruction
# 1) reading damage image
# 2) getting shape image
# 3) convert all pixel in damager image to our desired output
# 4) save the mask in .jpg format
import cv2
import numpy as np
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\cat_damaged.png'
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE) # gray scale image

# get shape image
height, width = image.shape[:2]
print(height)
print(width)

# convert all pixel greater than zero to black while black become white
for i in range(height):
    for j in range(width):
        # 3 value (BGR color space)
        if image[i, j] > 0: # sum > 0 then pixel is not pure black
            image[i, j] = 0 # sum > 0 change to black
        else:
            image[i, j] = [255, 255, 255] # sum = 0 change to white

# saving the mask
mask = image
cv2.imwrite("mask.jpg", mask)

# display mask
cv2.imshow("image_mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# repair image
# load image damage and mask before this

# I not have mask file in directory then use mask from process upper
image = cv2.imread(path)
#mask_path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\mask.jpg'
#mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
mask = cv2.imread("mask.jpg", cv2.IMREAD_GRAYSCALE)

# Inpaint
dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)

# output
cv2.imwrite('inpaint.jpg', dst)