# example code use for output picture
import cv2
path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geek1.png"
image = cv2.imread(path)
cv2.imshow("picture : ", image)
cv2.waitKey(0);
cv2.destroyAllWindows()

# output in grayscale mode (black and white picture)
image = cv2.imread(path, 0)
# number after path of picture is intensity of grayscale
# value between 0 to 255
# 0 => black , 255 => white (255 not work in code)
# not work because 255 is pixel intensity not flag value to use

# or use this code (same result)
image1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("image : ", image)
cv2.imshow("image1 : ", image1)
cv2.waitKey(0);
cv2.destroyAllWindows()

# comparison flag value (number) vs constant name (long command)
# 1 => cv2.IMREAD_COLOR
# 0 => cv2.IMREAD_GRAYSCALE
# -1 => cv2.IMREAD_UNCHANGED (include transparency if it have)

