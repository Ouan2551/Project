# import library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# use library cv2 to show picture
# read image not for get to use 'r' in front of directory picture
img = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geeksforgeeks.png"
                , cv2.IMREAD_COLOR)
# structure imshow(title gui window, image array)
cv2.imshow("image : ", img)
print(img.shape[:3]) # show size of image
cv2.waitKey(0) # wait user click to close window
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()

# use library matplotlib to show picture
img1 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geeksforgeeks.png")
plt.imshow(img1)
plt.waitforbuttonpress()
plt.close('all')

# the difference is cv2 use BGR color format
# but matplotlib use RGB color format
# and this is how to format BGR to RGB
RGB_convert_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_convert_img)
plt.waitforbuttonpress()
plt.close('all')