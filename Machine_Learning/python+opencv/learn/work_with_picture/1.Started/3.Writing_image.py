import cv2
import os
image_path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geek1.png"
directory = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started"

img = cv2.imread(image_path) # read image
os.chdir(directory) # specified directory

# list file in directory before save
print("Before saving image : ")
print(os.listdir(directory))

filename = 'SaveImage.jpg' # file name you want to save
filename1 = 'SaveImage1.jpg'
# use cv2.imwrite(filename you want to save, img you want to save)
# to save image to any storage device
cv2.imwrite(filename, img)
# save with custom quality (this command use 20% quality from original picture)
cv2.imwrite(filename1, img, [cv2.IMWRITE_JPEG_QUALITY, 20])
# save with black and white picture
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("SaveImage_black_and_White.jpg", gray_image)

#list file in directory after save
print("After saving image : ")
print(os.listdir(directory))

print("Successful save")

# cv2.imwrite() support .jpg .jpeg .png .tiff .tif. bmp .ppm .pgm