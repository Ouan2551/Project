# erosion => remove small white noise and shrinks bright regions in image
# object detection, background removal, noise reduction
import cv2
import numpy as np
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
window_name = "image"

# creating kernel
kernel = np.ones((5,5), np.uint8)

# use cv2.erode() method
image = cv2.erode(image, kernel)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()