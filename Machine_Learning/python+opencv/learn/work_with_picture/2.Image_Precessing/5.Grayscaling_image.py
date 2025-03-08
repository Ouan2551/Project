# convert other color space to shade of gray
# important from gray shade
# 1) reduce model complect 2) grayscale only have 1 dimension but RGB have 3 dimension
# 3) some algorithms work on grayscale image only

import cv2
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Method 1 (set gray scale using "cv2.cvtColor()")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Method 2 (set gray scale from read path picture)
image1 = cv2.imread(path, 0)
cv2.imshow("gray_image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Method 3 (using pixel manipulation)
(row, column) = image.shape[:2]
for i in range (row):
    for j in range (column):
        gray_image[i, j] = sum(image[i, j]) * 0.33

cv2.imshow("gray_image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()