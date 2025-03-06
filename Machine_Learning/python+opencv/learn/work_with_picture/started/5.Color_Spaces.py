#Color space => represent color channel give the image that particular hus
# e.g. 1) RGB(Red, Green, Blue) 2) CMYK (Cyan, Magenta, Yellow, Black)
# 3) HSV (Hue, Saturation, Value)
# RGB actually store color in BGR format (Blue, Green, REd)

import cv2

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geek1.png"
image = cv2.imread(path)
B, G, R = cv2.split(image)

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()