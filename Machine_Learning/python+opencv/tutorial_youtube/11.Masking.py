import cv2
import numpy as np
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cats.jpg'
image = cv2.imread(path)
cv2.imshow("image", image)

# 1) Masking => focus on image use with bitwise operation for better result

# if not use blank size equal image you will get error if you use masking
blank = np.zeros(shape=image.shape[:2], dtype='uint8')
cv2.imshow("blank", blank)

mask = cv2.circle(blank.copy(), center=(image.shape[1]//2, image.shape[0]//2), radius=100, color=255, thickness=-1)
cv2.imshow("mask", mask)

mask_image = cv2.bitwise_and(src1=image, src2=image, mask=mask)
cv2.imshow("mask_image", mask_image)

# 2) Masking but with 2 shape
circle = cv2.circle(blank.copy(), center=(image.shape[1]//2, image.shape[0]//2), radius=100, color=255, thickness=-1)
rectangle = cv2.rectangle(blank.copy(), pt1=(100, 100), pt2=(400, 400), color=255, thickness=-1)
# not mask
mix_shape = cv2.bitwise_and(circle, rectangle)
cv2.imshow("mix_shape", mix_shape)
# with mask
mask_shape = cv2.bitwise_and(image, image, mask=mix_shape)
cv2.imshow("mix_shape_with_mask", mask_shape)
if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()