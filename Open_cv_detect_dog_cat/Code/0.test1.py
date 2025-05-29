import cv2
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore

# Load model
model = load_model(r"C:\Important files Nannaphat\coding\Project\Open_cv_detect_dog_cat\model\dog_cat_model2.h5")
model.summary()

# Class names
classes = ["Cat", "Dog"]
image_size = (80, 80)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize to match model input
    resized = cv2.resize(gray, image_size)

    # Preprocess
    img = resized.reshape(-1, image_size[0], image_size[1], 1)
    img = img / 255.0

    # Predict
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    confidence = prediction[0][predicted_class]

    # Display label
    label = f"{classes[predicted_class]} ({confidence*100:.2f}%)"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Dog vs Cat Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()
