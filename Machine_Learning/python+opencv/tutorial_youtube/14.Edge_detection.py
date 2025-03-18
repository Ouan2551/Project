import cv2
import numpy as np

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cats.jpg'
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

# Laplacian
lap = cv2.Laplacian(gray_image, ddepth=cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("laplacian", lap)

# Sobel
sobel_X = cv2.Sobel(gray_image, ddepth=cv2.CV_64F, dx=1, dy=0,)
sobel_Y = cv2.Sobel(gray_image, ddepth=cv2.CV_64F, dx=0, dy=1,)
combined_sobel = cv2.bitwise_or(sobel_X, sobel_Y)
cv2.imshow("sobel_X", sobel_X)
cv2.imshow("sobel_Y", sobel_Y)
cv2.imshow("combined_sobel", combined_sobel)

# just use canny for compare
canny = cv2.Canny(gray_image, threshold1=150, threshold2=175)
cv2.imshow("canny", canny)
if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()