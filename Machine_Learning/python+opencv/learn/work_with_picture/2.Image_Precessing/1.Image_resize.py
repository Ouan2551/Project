# Image resize => help reduce time to train neural network
import cv2
import matplotlib.pyplot as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)
print(image.shape[:2]) # output original width and height picture

half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image,(423, 1200))
stretch_near = cv2.resize(image, (450, 1100), interpolation=cv2.INTER_LINEAR)

titles = ["Original", "Half", "Bigger", "Stretch_Near"]
images = [image, half, bigger, stretch_near]
count = len(images)

# output
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()