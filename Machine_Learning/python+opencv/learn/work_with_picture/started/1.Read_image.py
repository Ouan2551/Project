# import library
import cv2

# read image not for get to use 'r' in front of directory picture
img = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geeksforgeeks.png"
                , cv2.IMREAD_COLOR)

# structure imshow(title gui window, image array)
cv2.imshow("image : ", img)

# just show size of image

print(img.shape[:3])

# wait user click to close window
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()