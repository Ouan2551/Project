import cv2
import numpy as np

# import haar_face.xml using for detect face
path_haar_face_xml = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\harr_face.xml'
haar_face_cascade = cv2.CascadeClassifier(path_haar_face_xml)

# load file creat from "1.Face_train.py"
path_features = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\features.npy'
features = np.load(path_features)
path_labels = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\labels.npy'
labels = np.load(path_labels)

face_recognize = cv2.face.LBPHFaceRecognizer_create()
face_recognize_path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\face_trained.yml'
face_recognize.read(face_recognize_path)

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

# import image you want to detect
path_image = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\16.Face_Recognize\Faces\val\ben_afflek\1.jpg'
image = cv2.imread(path_image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("person", gray_image)

# detect zone
faces_rect = haar_face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)
for (x,y,h,w) in face_recognize(faces_rect):
    faces_roi = gray_image[y:y+h, x:x+w]
    
    label, confidence = face_recognize.predict(faces_roi)
    print("label = ", people[label], " with a confidence of = ", confidence)
    
    cv2.putText(image, text=str(people[label]), org=(20,20), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0
                , color=(0,255,0), thickness=2)
    cv2.rectangle(image, pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=2)
    
cv2.imshow("detective", image)

if cv2.waitKey(0) & 0xFF == ord('d'):
    cv2.destroyAllWindows()