# test_yolo.py
import torch
from PIL import Image

# Load the YOLOv5 model (small version)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # You can also use 'yolov5m', 'yolov5l', 'yolov5x'

# Load an image
# C:\Users\kisho\Desktop\Data-Dynos\backend\
image_path = 'C:/Users/kisho/Desktop/Data-Dynos/backend/man.jpg' # Replace with your test image path
image = Image.open(image_path)

# Perform inference with the model
results = model(image)

# Show the image with detected bounding boxes
results.show()

# Print detected objects with confidence scores
print(results.pandas().xywh[0])  # Print results in a pandas DataFrame format
