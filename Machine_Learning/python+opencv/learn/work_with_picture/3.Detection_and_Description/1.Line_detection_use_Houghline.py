# Hough Transform method use in image for detect shape
# if shape can represented in mathematical form

import cv2
import numpy as np

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply edge detection method on image
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

# return array of r and theta value
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# loop run till r and theta value in range 2d array
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    
    # store value of cos(theta) in a
    a = np.cos(theta)
    
    # store value of sin(theta) in b
    b = np.sin(theta)
    
    # x0 store the value r_cos(theta)
    x0 = a*r
    
    # y0 store the value r_sin(theta)
    y0 = b*r
    
        # x1 stores the rounded off value of (r_cos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))

    # y1 stores the rounded off value of (r_sin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))

    # x2 stores the rounded off value of (r_cos(theta)+1000sin(theta))
    x2 = int(x0 - 1000*(-b))

    # y2 stores the rounded off value of (r_sin(theta)-1000cos(theta))
    y2 = int(y0 - 1000*(a))

    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be
    # drawn. In this case, it is red.
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()