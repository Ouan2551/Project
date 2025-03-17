import cv2

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cats.jpg'
image = cv2.imread(path)

# 1) Averaging => define kernel window over specific portion in image (very basic method blur)
# how this do blur => replace every pixel with average pixel value
# ksize => matrix use for calculate pixel average (size neighborhood for calculate)
# if you have ksize = 3,3 then it use pixel 9 pixel from kernel to calculate
average = cv2.blur(image, ksize=(3,3))
cv2.imshow("average_blur", average)

# 2) Gaussian Blur => more natural averaging blur it calculate like averaging blur
# but it will get more weight when pixel closer center and lower weight when far from center
gaussian = cv2.GaussianBlur(image, ksize=(3,3), sigmaX=0)
# sigmaX => control amount blur (set value to 0 mean it will control blur auto)
cv2.imshow("gaussian", gaussian)

# 3) Median Blur => like averaging blur but it find median value
median = cv2.medianBlur(image, ksize=7)
# use 3 (integer) not (3,3) (tuple) but it same but in another way
cv2.imshow("median", median)

# 4) bilateral
bilateral = cv2.bilateralFilter(image, d=5, sigmaColor=15, sigmaSpace=15)
# d=5 is same ksize but it integer not tuple
# sigmaColor = 15 color pixel value that have significant influence
# sigmaSpace = 15 pixel have distant 15 pixel from center will have significant influence
cv2.imshow("bilateral", bilateral)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()