from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO

# Load the model and processor from Hugging Face
processor = AutoImageProcessor.from_pretrained("taroii/pothole-detection-model")
model = AutoModelForImageClassification.from_pretrained("taroii/pothole-detection-model")

# Hardcoded image path
image_path = "a2.jpg"  # Replace with your hardcoded image path
image = Image.open(image_path)

# Preprocess the image
inputs = processor(images=image, return_tensors="pt")

# Run the model to make predictions
outputs = model(**inputs)

# Get the predicted class
predicted_class = outputs.logits.argmax(-1).item()

# Print the predicted class
print(f"Predicted class: {predicted_class}")

# Function to assign priority based on the prediction
def assign_priority(predicted_class):
    if predicted_class == 1:
        return "Normal"
    return None  # You can change this based on other predictions

priority_label = assign_priority(predicted_class)
def send_email_to_admin(image_file):
    admin_email = "kishorekumars5643@gmail.com"  # Replace with the admin's email
    sender_email = "kkishore51565@gmail.com"  # Replace with your email
    password = "dlku apwt kqhl eyxy" # Use an app password or an SMTP password (not your main email password)
    
    # Formal complaint email content
    category = "Pothole" if predicted_class == 1 else None  # Based on predicted class
    subject = f"Formal Complaint: Environmental Hazard Detected - {category}"
    
    body = f"""
    Dear Sir/Madam,

    I hope this message finds you well. I am writing to bring to your attention an environmental issue that has been detected in the vicinity. 
    This issue pertains to a {category} that poses a serious safety risk to the public and needs immediate attention.

    The attached image provides a clear view of the situation. It is crucial that this matter be addressed promptly to prevent any further accidents or complications. 
    As a responsible citizen, I urge you to prioritize the resolution of this environmental hazard.

    **Priority**: {priority_label}
    
    We look forward to your swift action in addressing this pressing concern.

    Thank you for your prompt attention to this matter.
    """

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = admin_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    img_byte_arr = BytesIO()
    image_file.seek(0)  # Ensure the file pointer is at the start
    img_data = image_file.read()  # Read the image data
    img_byte_arr.write(img_data)
    img_byte_arr.seek(0)

    img_attachment = MIMEImage(img_byte_arr.read(), name="pothole_image.jpg")
    msg.attach(img_attachment)

    # Send the email
    try:
        # Establish connection to SMTP server (using Gmail in this case)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log into the email account
        server.sendmail(sender_email, admin_email, msg.as_string())  # Send the email
        server.quit()  # Close the connection
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

# If the prediction class is 1, send the email
if predicted_class == 1:
    print("New environmental issue detected, sending formal complaint email to admin...")
    
    # Open the image and send it as email attachment
    with open(image_path, 'rb') as image_file:
        send_email_to_admin(image_file)
