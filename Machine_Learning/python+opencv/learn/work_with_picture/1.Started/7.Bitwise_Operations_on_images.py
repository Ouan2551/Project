# Bitwise operations => and, or, xor, not

import cv2

image5 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i5.png")
image6 = cv2.imread(r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\i6.png")

cv2.imshow("image5 : ", image5)
cv2.waitKey(0)
cv2.imshow("image6 : ", image6)
cv2.waitKey(0)

# 1) And Operations
And_image = cv2.bitwise_and(image5, image6, mask=None)
cv2.imshow("And_image : ", And_image)
cv2.waitKey(0)

# 2) Or Operations
Or_image = cv2.bitwise_or(image5, image6, mask=None)
cv2.imshow("Or_image : ", Or_image)
cv2.waitKey(0)

# 3) XOr Operations
XOr_image = cv2.bitwise_xor(image5, image6, mask=None)
cv2.imshow("Xor_image : ", XOr_image)
cv2.waitKey(0)

# 4) Not Operations
Not_image5 = cv2.bitwise_not(image5, mask=None)
Not_image6 = cv2.bitwise_not(image6, mask=None)

cv2.imshow("Not_image5 : ", Not_image5)
cv2.waitKey(0)
cv2.imshow("Not_image6 : ", Not_image6)
cv2.waitKey(0)

cv2.destroyAllWindows()

# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows() 