import cv2
import numpy as np

# contours => useful tool for get shape analysis and object detection

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)
cv2.imshow("Image_original", image)

blank = np.zeros(shape=image.shape, dtype='uint8')
cv2.imshow("blank", blank)

# before do this convert picture to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_image)

# blur image for decrease contours found
blur_image = cv2.blur(gray_image, ksize=(5,5), dst=cv2.BORDER_DEFAULT)
cv2.imshow("blur_image", blur_image)

# canny use for process object detection
canny_no_blur = cv2.Canny(image, 125, 175)
cv2.imshow("canny_no_blur", canny_no_blur)
canny_with_blur = cv2.Canny(blur_image, 125, 175)
cv2.imshow("canny_with_blur", canny_with_blur)

ret, thresh = cv2.threshold(gray_image, thresh=125, maxval=255, type=cv2.THRESH_BINARY)
# in type= just method use for to set pixel value
cv2.imshow("thresh", thresh)
# if value < 125 will set color to black
# if value > 255 will set color to white

contour_no_blur, hierarchies = cv2.findContours(canny_no_blur, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
contour_with_blur, hierarchies = cv2.findContours(canny_with_blur, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
contour_with_thresh = cv2.findContours(thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
# contour this variable like list of contour fount in image
# hierarchies => found contour but in image have multiple of shape
print(len(contour_no_blur), "contour(s) found [no_blur]")
print(len(contour_with_blur), "contour(s) found [with_blur]")
print(len(contour_with_thresh), "contour(s) found [with_thresh]")

# work with blank
cv2.drawContours(image=blank, contours=contour_no_blur, contourIdx=-1, color=(0,0,255), thickness=1)
cv2.imshow("contour draw", blank)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()