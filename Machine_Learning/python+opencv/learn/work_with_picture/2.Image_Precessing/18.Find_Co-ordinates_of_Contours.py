# Contours are defined as the line joining all the points
# alone the boundary of image have same intensity
# come handle in shape analysis finding the size of object or detection object

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\image1.jpg'
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# convert image to binary image (gray scale only)
_, threshold = cv2.threshold(image_gray, 110, 255, cv2.THRESH_BINARY)

# detect contours (contours is same meaning shape) in image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# going to every contours found in image
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
    
    # draw boundary of contours
    cv2.drawContours(image_gray, [approx], 0, (0, 0, 255), 5)
    
    # the co-ordinates of teh vertices
    n = approx.ravel()
    i = 0
    
    for j in n:
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
            
            # String contain co-ordinate
            string = str(x) + " " + str(y)
            
            if (i == 0):
                # text on topmost co-ordinate
                cv2.putText(image_gray, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
            else:
                # text on remaining co-ordinate
                cv2.putText(image_gray, string, (x, y), font, 0.5, (0, 255, 0))
        i = i + 1

cv2.imshow("image", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()