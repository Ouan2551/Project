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
# value more than 150 set to 255 (pixel intensity)
cv2.imshow("simple_thresholding", thresh)
# inverse
threshold, thresh_inverse = cv2.threshold(gray_image, thresh=150, maxval=255, type=cv2.THRESH_BINARY_INV)
# value less than 150 set to 255 (pixel intensity)
cv2.imshow("simple_thresholding_inverse", thresh_inverse)

# 2) adaptive thresholding
adaptive = cv2.adaptiveThreshold(gray_image, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=3)
cv2.imshow("adaptive_thresholding", adaptive)
adaptive_inverse = cv2.adaptiveThreshold(gray_image, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY_INV, blockSize=11, C=3)
cv2.imshow("adaptive_thresholding_inverse", adaptive_inverse)
# Gaussian
adaptive_gaussian = cv2.adaptiveThreshold(gray_image, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=3)
cv2.imshow("adaptive_thresholding_gaussian", adaptive_gaussian)
adaptive_inverse_gaussian = cv2.adaptiveThreshold(gray_image, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY_INV, blockSize=11, C=3)
cv2.imshow("adaptive_thresholding_inverse_gaussian", adaptive_inverse_gaussian)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()