# use for smoothening image and reduce noise
import cv2
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\taj.jpg'
image = cv2.imread(path)

# apply bilateral filter with d = 15, sigmaColor = sigmaSpace = 75
bilateral = cv2.bilateralFilter(image, 15, 75, 75)

cv2.imshow("original", image)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()