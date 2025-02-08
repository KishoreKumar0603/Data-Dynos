from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # 'n' = nano, you can use 's', 'm', 'l' for larger models

# Train the model
model.train(data="C:/Users/kisho/Desktop/Data-Dynos/backend/yolo_model/pothole_dataset/data.yaml", epochs=50, batch=16, imgsz=640)
