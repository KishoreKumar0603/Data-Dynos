from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import requests

# Load the model and processor from Hugging Face
processor = AutoImageProcessor.from_pretrained("taroii/pothole-detection-model")
model = AutoModelForImageClassification.from_pretrained("taroii/pothole-detection-model")

image = Image.open("a2.jpg")


# Preprocess the image
inputs = processor(images=image, return_tensors="pt")

# Run the model to make predictions
outputs = model(**inputs)

# Get the predicted class
predicted_class = outputs.logits.argmax(-1).item()

# Print the predicted class
print(f"Predicted class: {predicted_class}")
