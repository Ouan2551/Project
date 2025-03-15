import cv2
# or import cv2 as cv (short command use)
import numpy as np

# 3 is color channel
# at blank create area for shape
blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow("blank", blank)

# 1) paint image a certain color
# from BGR value => 0, 0, 0 (blue, green, red)
blank[:] = 255, 0, 0
cv2.imshow("blue", blank)
blank[:] = 0, 255, 0
cv2.imshow("green", blank)
blank[:] = 0, 0, 255
cv2.imshow("red", blank)

# Create a NEW blank image for the small red rectangle
# if not create new blank you will get normal size of shape not small size
blank_small_red = np.zeros((500, 500, 3), dtype='uint8')

# Create the small red rectangle
blank_small_red[0:100, 0:100] = 0, 0, 255
cv2.imshow("small red", blank_small_red)  # Display the NEW image

# 2) Draw a rectangle (area_want_to_draw, start_location, stop_location, color, thickness, line_type)
cv2.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv2.imshow("rectangle", blank)
# fill rectangle
cv2.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv2.FILLED) # or "cv2.FILLED" use '-1' instead
cv2.imshow("rectangle_fill", blank)
# rectangle but 1/2 size of blank (area you want to draw)
cv2.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=-1)
cv2.imshow("rectangle_half", blank)

# 3) Draw a circle
# create new clean blank
blank_circle = np.zeros((500, 500 , 3), dtype = 'uint8')
cv2.circle(blank_circle, (250, 250), radius= 10, color=(0, 0, 255), thickness=1)
cv2.imshow("circle", blank_circle)
# fill circle
cv2.circle(blank_circle, (250, 250), radius= 10, color=(0, 0, 255), thickness=-1)
cv2.imshow("circle", blank_circle)

# 4) Draw a line
blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), color=(0, 255, 255), thickness=1)
cv2.imshow("line", blank)

# write text
cv2.putText(blank, "Hello", org=(250, 250), fontScale=1.0, color=(255, 0, 0), thickness=2, fontFace=cv2.FONT_HERSHEY_COMPLEX)
cv2.imshow("text", blank)


path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)
cv2.imshow("image", image)
if cv2.waitKey() & 0xFF == ord('d'):
    cv2.destroyAllWindows()