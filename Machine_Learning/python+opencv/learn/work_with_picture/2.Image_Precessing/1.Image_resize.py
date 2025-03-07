# Image resize => help reduce time to train neural network
import cv2
import matplotlib as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\started\geeksforgeeks.png"
image = cv2.imread(path)
print(image.shape[:2]) # output original shape picture
half = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image,())