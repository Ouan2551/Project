import cv2
import numpy as np

# Path to the damaged image
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\cat_damaged.png'

# Read the image as grayscale (to create mask)
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Get shape of image
height, width = image.shape[:2]
print(f"Image Size: {height}x{width}")

# Convert all non-black pixels to white (create mask)
_, mask = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

# Save the mask
cv2.imwrite("mask.jpg", mask)

# Display the mask
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reload the original damaged image (in color)
image = cv2.imread(path)

# Load mask as grayscale (to ensure it's in the correct format)
mask = cv2.imread("mask.jpg", cv2.IMREAD_GRAYSCALE)

# Perform inpainting (restore the image)
dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)

# Save and display the repaired image
cv2.imwrite("inpaint.jpg", dst)
cv2.imshow("Repaired Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()