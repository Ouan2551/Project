import cv2

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

# normal image
cv2.imshow("Image : ", image)
cv2.waitKey(0)

# image with border
image_border = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
cv2.imshow("Image Border : ", image_border)
cv2.waitKey(0)
cv2.destroyAllWindows()