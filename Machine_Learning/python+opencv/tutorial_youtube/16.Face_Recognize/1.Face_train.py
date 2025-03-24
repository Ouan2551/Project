import os
import cv2
import cv2.face
import numpy as np

# list people
# create list people by type yourself
people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
# base folder
DIR = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\Faces\train'

# or using loop to input list people (good for big data)
p = []
path_people = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\Faces\train'
for i in os.listdir(path_people):
    p.append(i)
print(p)

# import haar_face.xml using for detect face
path_haar_face_xml = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\harr_face.xml'
haar_face_cascade = cv2.CascadeClassifier(path_haar_face_xml)

features = [] # image array list
labels = []
def create_train():
    # loop in every folder
    for person  in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        # loop in every picture
        for image in os.listdir(path):
            image_path = os.path.join(path, image)
            
            # read image from path
            image_array = cv2.imread(image_path)
            # convert to gray scale 
            gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
            
            face_rect = haar_face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in face_rect:
                face_roi = gray_image[y:y+h, x:x+w] # face region of interest
                features.append(face_roi)
                labels.append(label)

# run function
create_train()
print("Train Done")

# use for check detect
print("Length of the features : ", len(features))
print("Length of the labels : ", len(labels))

# convert features list and labels to numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognize = cv2.face.LBPHFaceRecognizer_create()

# Train recognize on the features list and labels list
face_recognize.train(features, labels)
face_recognize.save("face_trained.yml")

np.save("features.npy", features)
np.save("labels.npy", labels)