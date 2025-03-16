import cv2
import matplotlib.pyplot as plt # use for BGR to RGB (RGB like convert of BGR)

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)

# 1) normal picture (BGR)
cv2.imshow("original", image)

# 2) convert BGR to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

# 3) BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_image", hsv_image)

# 4) BGR to LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("lab_image", lab_image)

# 5) BGR to RGB
# just output
plt.imshow(image)
plt.show()

# convert
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("rgb_image", rgb_image)
# or output with matplotlib
plt.imshow(rgb_image)
plt.show()

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()