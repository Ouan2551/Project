from ultralytics import YOLO

# Load YOLO model (pretrained)
model = YOLO("yolov8n.pt")

# Train the model
model.train(data="dataset/data.yaml", epochs=50, imgsz=640, batch=16)

# Save the trained model
model.export(format="onnx")  # Export to ONNX for deployment (optional)