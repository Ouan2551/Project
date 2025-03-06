#Arithmetic Operations like addition, subtraction and bitwise operation
#(and, or, not, xor) can be apply to input image

import cv2
import numpy as np

# 1) Addition image
# Syntax : cv2.add(img1, img2)
image1 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i1.jpg")
image2 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i2.jpg")

cv2.imshow("image1 : ",image1)
cv2.waitKey(0)
cv2.imshow("image2 : ",image2)
cv2.waitKey(0)

# structure cv2.addWeighted(image1, weight_image1, image2, weight_image2,
# brightness_adjustment)
addition_picture = cv2.addWeighted(image1, 0.5, image2, 0.4, 1)
cv2.imshow("mix image : ", addition_picture)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2) Subtraction image
image3 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i3.jpg")
image4 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i4.jpg")

cv2.imshow("image3 : ", image3)
cv2.waitKey(0)
cv2.imshow("image4 : ", image4)
cv2.waitKey(0)

subtraction_picture = cv2.subtract(image3, image4)
cv2.imshow("subtraction_picture : ", subtraction_picture)
cv2.destroyAllWindows()

# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  