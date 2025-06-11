import cv2
import numpy as np
from tensorflow.keras.models import load_model #type: ignore

# load model from patch
loaded_model = load_model(r"C:\Important files Nannaphat\coding\Project\student_chk\model\detect_people_model1.h5")

# output to check model
loaded_model.summary()

# class
characters = ["Boeing", "Ouan", "Third"]
image_size = (80, 80)
img = cv2.imread(r"C:\Important files Nannaphat\coding\Project\student_chk\DATA\Ouan\2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, image_size)  # resize image
img = img.reshape(-1, image_size[0], image_size[1], 1)  # reshape image
img = img / 255.0  # normalize image

prediction = loaded_model.predict(img)
predicted_class = np.argmax(prediction)

print("Predicted class:", characters[predicted_class])