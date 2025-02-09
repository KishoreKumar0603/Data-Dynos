from ultralytics import YOLO

model = YOLO("yolov8n.pt") 
model.train(data="C:/Users/kisho/Desktop/Data-Dynos/backend/yolo_model/pothole_dataset/data.yaml", epochs=50, batch=16, imgsz=640)
