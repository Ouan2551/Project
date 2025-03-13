# apply transform image for contrast manipulation
# common intensity transformation by this
# 1) Image Negatives (Linear)
# 2) Log Transformations
# 3) Power-Law (Gamma) Transformations
# 4) Piecewise-Linear Transformations Functions

import cv2
import numpy as np

path =  r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\sample.jpg'
image = cv2.imread(path)

# 1) Log Transformations
c = 255/(np.log(1 + np.max(image)))
# np.max(image) use for find maximum pixel value in image
log_transformed = c * np.log(1 + image)

# specify data type
log_transformed = np.array(log_transformed, dtype = np.uint8)

cv2.imshow("log_transformed", log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2) Power-law (Gamma) Transformations
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # apply gamma correction
    gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = np.uint8)
    
    # save image
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected) 
    cv2.imshow("gamma_corrected" + str(gamma), gamma_corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 3) Piecewise Linear Transformation Functions
# Function to map each intensity level to output intensity level. 
def pixelVal(pix, r1, s1, r2, s2): 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 
    
# Define parameters. 
r1 = 70
s1 = 0
r2 = 140
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array. 
pixelVal_vec = np.vectorize(pixelVal) 

# Apply contrast stretching. 
contrast_stretched = pixelVal_vec(image, r1, s1, r2, s2) 

# Save edited image. 
cv2.imshow("contrast", contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()