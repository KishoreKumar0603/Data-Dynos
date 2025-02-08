# /backend/ml_model/yolo_model.py
import torch
from PIL import Image
import io

# Load YOLOv5 pre-trained model (v5 is the version we're using)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' is the small version, you can use other versions like 'yolov5m'

# Define the function to process the image and get predictions
def get_image_predictions(image_data):
    # Convert image to PIL format
    image = Image.open(io.BytesIO(image_data))
    
    # Perform inference with YOLOv5
    results = model(image)
    
    # Parse the results
    predictions = results.pandas().xywh[0]  # Get predictions in pandas DataFrame format
    
    # Return predictions and confidence score (e.g., class of environmental issue)
    return predictions[['class', 'name', 'confidence']]  # 'name' is the label of the detected class
