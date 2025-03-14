import cv2
import matplotlib.pyplot as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

layer = image.copy()

for i in range(4):
    plt.subplot(2, 2, i + 1)
    
    # use pyrDown() function
    layer = cv2.pyrDown(layer)
    
    plt.imshow(layer)
    cv2.imshow("str(i)", layer)
    cv2.waitKey(0)

cv2.destroyAllWindows()