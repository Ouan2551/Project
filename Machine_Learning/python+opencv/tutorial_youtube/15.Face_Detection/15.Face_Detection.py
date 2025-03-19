# follow this url for haarcascades
# https://github.com/opencv/opencv/tree/4.x/data/haarcascades

import cv2
# setup
path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\Photos\group 1.jpg'
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# import xml file
path_haar_face_xml = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\15.Face_Detection\harr_face.xml'
haar_face_cascade = cv2.CascadeClassifier(path_haar_face_xml)

# detective
face_rect = haar_face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1)
print("Number face found : ", len(face_rect))

# draw rectangle over face
for (x, y, w, h) in face_rect:
    cv2.rectangle(image, pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=2)
cv2.imshow("Detective", image)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()