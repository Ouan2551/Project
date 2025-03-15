import cv2

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)
cv2.imshow("original", image)

# 1) Convert to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray_image)

# 2) Blur image (ksize is increase or decrease blur in odd number only)
blur_image = cv2.GaussianBlur(image, ksize=(3,3), sigmaX=cv2.BORDER_DEFAULT)
cv2.imshow("blur" ,blur_image)

# 3) Edge Cascade
canny = cv2.Canny(image, 125, 175)
cv2.imshow("Edge Cascade", canny)
# blur version
canny_blur = cv2.Canny(blur_image, 125, 175)
cv2.imshow("Edge Cascade with blur", canny_blur)

# 4) Dilating image => make object size bigger
dilated = cv2.dilate(canny, kernel=(3,3), iterations=3)
cv2.imshow("dilated", dilated)

# 5) Eroding => make object size smaller
eroded = cv2.erode(dilated, kernel=(3,3), iterations=3)
cv2.imshow("eroded", eroded)

# 6) Resize
resize_normal = cv2.resize(image, dsize=(500,500))
cv2.imshow("resize_normal", resize_normal)
resize_Inter_Area = cv2.resize(image, dsize=(500,500), interpolation=cv2.INTER_AREA)
cv2.imshow("resize_Inter_Area", resize_Inter_Area)
resize_Inter_Cubic = cv2.resize(image, dsize=(500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resize_Inter_Cubic", resize_Inter_Cubic)

# 7) Cropping (50:200 mean select between 50 to 199) think like (x, y) to crop image
crop = image[50:200, 200:400]
cv2.imshow("crop_image", crop)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()