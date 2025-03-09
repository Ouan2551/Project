import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

# 1) Image Resizing
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

scale_factor1 = 3.0 # increase size
scale_factor2 = 1/3.0 # decrease size
height, width = image_rgb.shape[:2]

# use scale_factor1
new_height = int(height * scale_factor1)
new_width = int(width * scale_factor1)

# resize image
zoomed_image = cv2.resize(src = image_rgb, dsize=(new_height, new_width))
interpolation = cv2.INTER_CUBIC

# use scale_factor2
new_height1 = int(height * scale_factor2)
new_width1 = int(width * scale_factor2)

# scaled image
scaled_image = cv2.resize(src = image_rgb, dsize = (new_height1, new_width1))
interpolation = cv2.INTER_AREA

# create subplots
fig, axs = plt.subplots(1, 3, figsize = (10, 4))

# plot original image
axs[0].imshow(image_rgb)
axs[0].set_title("Original Image Shape : "+str(image_rgb.shape))

# plot zoom image
axs[1].imshow(zoomed_image)
axs[1].set_title("Zoom Image Shape : "+str(zoomed_image.shape))

# plot scale image
axs[2].imshow(scaled_image)
axs[2].set_title("Scale_Image Shape : "+str(scaled_image.shape))

plt.tight_layout()
plt.show()