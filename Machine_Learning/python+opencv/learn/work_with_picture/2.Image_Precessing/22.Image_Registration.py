# image processing technical to align different image of same scene
# like you want to change photo from different view to same view
import cv2
import numpy as np
path1 = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\align.jpg'
path2 = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\learn\work_with_picture\2.Image_Precessing\ref.jpg'
photo1 = cv2.imread(path1)
photo2 = cv2.imread(path2)
height, width = photo2.shape[:2]

# convert to grayscale
gray1 = cv2.cvtColor(photo1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(photo2, cv2.COLOR_BGR2GRAY)

# create ORB detector with 5000 features
orb_detector = cv2.ORB_create(10000)

# find keypoints and descriptors
kp1, d1 = orb_detector.detectAndCompute(gray1, None)
kp2, d2 = orb_detector.detectAndCompute(gray2, None)

# match feature between 2 image
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# match two set of descriptors
matches = matcher.match(d1, d2)

# sort matches on the basic of their hamming distance
matches.sort(key = lambda x: x.distance)

# take the top 90% matches forward
matches = matches[:int(len(matches)*0.9)]
no_of_matches = len(matches)

# Define empty matrices of shape no_of_matches * 2
p1 = np.zeros((no_of_matches, 2))
p2 = np.zeros((no_of_matches, 2))

for i in range(len(matches)):
    p1[i, :] = kp1[matches[i].queryIdx].pt
    p2[i, :] = kp2[matches[i].queryIdx].pt

# find the homography matrix
homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

# use this matrix to transforms the color image wrt the reference image
transformed_image = cv2.warpPerspective(photo1, homography, (width, height))

# output
cv2.imshow("transformed_image", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()