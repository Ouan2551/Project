import cv2
import numpy as np

path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\cat.jpg'
image = cv2.imread(path)


b, g, r = cv2.split(image)

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

print(image.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# mix b, g, r into 1 image
merged = cv2.merge([b,g,r])
cv2.imshow("merged", merged)

# use blank to display image but only 1 color channel
blank = np.zeros(shape=image.shape[:2], dtype='uint8')
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])
cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()