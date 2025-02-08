import os
import shutil
import random
import xml.etree.ElementTree as ET

# Paths
dataset_path = "C:/Users/kisho/Desktop/Data-Dynos/dataset"  # Original dataset folder (contains both images and XML files)
pothole_dataset_path = "C:/Users/kisho/Desktop/Data-Dynos/backend/yolo_model/pothole_dataset"  # Destination folder

train_path = os.path.join(pothole_dataset_path, "train")
val_path = os.path.join(pothole_dataset_path, "val")

# Create train/val structure
os.makedirs(os.path.join(train_path, "images"), exist_ok=True)
os.makedirs(os.path.join(train_path, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_path, "images"), exist_ok=True)
os.makedirs(os.path.join(val_path, "labels"), exist_ok=True)

# Function to convert Pascal VOC XML to YOLO format
def convert_xml_to_yolo(xml_path, output_path, img_width, img_height):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    with open(output_path, 'w') as yolo_annotation:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            class_id = 0  # Assuming class ID is 0 for pothole

            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            center_x = (xmin + xmax) / 2 / img_width
            center_y = (ymin + ymax) / 2 / img_height
            width = (xmax - xmin) / img_width
            height = (ymax - ymin) / img_height

            yolo_annotation.write(f"{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}\n")

# Collect all image and XML annotation files
image_files = [f for f in os.listdir(dataset_path) if f.endswith(('.jpg', '.png'))]
xml_files = {f.replace('.xml', ''): f for f in os.listdir(dataset_path) if f.endswith('.xml')}

# Shuffle dataset
random.shuffle(image_files)

# Split into train (80%) and val (20%)
split_ratio = 0.8
train_size = int(len(image_files) * split_ratio)
train_images = image_files[:train_size]
val_images = image_files[train_size:]

# Image dimensions (update if necessary)
image_width, image_height = 1920, 1080

# Process files
for image in image_files:
    image_name = os.path.splitext(image)[0]
    xml_file = xml_files.get(image_name, None)  # Get corresponding XML file

    # Determine destination (train or val)
    if image in train_images:
        image_dest = os.path.join(train_path, "images", image)
        label_dest = os.path.join(train_path, "labels", f"{image_name}.txt")
    else:
        image_dest = os.path.join(val_path, "images", image)
        label_dest = os.path.join(val_path, "labels", f"{image_name}.txt")

    # Move image
    shutil.move(os.path.join(dataset_path, image), image_dest)

    # Convert XML to YOLO and move label (if annotation exists)
    if xml_file:
        convert_xml_to_yolo(os.path.join(dataset_path, xml_file), label_dest, image_width, image_height)
        os.remove(os.path.join(dataset_path, xml_file))  # Remove original XML file after conversion

print(f"✅ Dataset processing complete! {len(train_images)} images in train, {len(val_images)} in val.")
