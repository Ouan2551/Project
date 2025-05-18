import cv2
import numpy as np
from tensorflow.keras.models import load_model #type: ignore

# Load your model
loaded_model = load_model(r"C:\Important files Nannaphat\coding\Project\Open_cv_detect_dog_cat\model\dog_cat_model1.h5")

# Class names
characters = ["Cat", "Dog"]
image_size = (80, 80)

# Read image
img = cv2.imread(r"C:\Important files Nannaphat\picture\1736774455395.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_resized = cv2.resize(img_gray, image_size)  # Resize for model input

# Prepare image for prediction
img_input = img_resized.reshape(-1, image_size[0], image_size[1], 1) / 255.0

# Predict class
prediction = loaded_model.predict(img_input)
predicted_class = np.argmax(prediction)
label = characters[predicted_class]

# Draw rectangle around the whole image
height, width, _ = img.shape
start_point = (0, 0)
end_point = (width - 1, height - 1)
color = (0, 255, 0)  # Green color for rectangle
thickness = 2

cv2.rectangle(img, start_point, end_point, color, thickness)

# Put text (label) on top-left corner
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text_color = (0, 255, 0)

# Position for text
text_position = (10, 30)
cv2.putText(img, label, text_position, font, font_scale, text_color, font_thickness)

# Show image
cv2.imshow("Prediction", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
