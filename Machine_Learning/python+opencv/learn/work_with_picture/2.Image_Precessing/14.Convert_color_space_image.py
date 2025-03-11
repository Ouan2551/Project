import cv2

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

# convert to gray scale image
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# convert to HSV color space
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("original_image : ", image)
cv2.imshow("image_gray : ", image_gray)
cv2.imshow("image_HSV : ", image_HSV)
cv2.waitKey(0)
cv2.destroyAllWindows()