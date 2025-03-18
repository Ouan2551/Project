import cv2

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cats.jpg'
image = cv2.imread(path)
cv2.imshow("image", image)

# convert image to gray scale before doing
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray_image)

# Thresholding => convert image to binary
# 1) simple thresholding
threshold, thresh = cv2.threshold(gray_image, thresh=150, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow("simple_thresholding", thresh)
# inverse
threshold, thresh_inverse = cv2.threshold(gray_image, thresh=150, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow("simple_thresholding_inverse", thresh_inverse)
if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()