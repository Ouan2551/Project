# made or reduce noisy image for analyze image better
import numpy as np
import cv2
import matplotlib.pyplot as plt

path = r"D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\geeksforgeeks.png"
image = cv2.imread(path)

reduce_noise = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
plt.subplot(121), plt.imshow(image)
plt.subplot(122), plt.imshow(reduce_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()