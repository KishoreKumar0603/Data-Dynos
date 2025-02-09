from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
processor = AutoImageProcessor.from_pretrained("taroii/pothole-detection-model")
model = AutoModelForImageClassification.from_pretrained("taroii/pothole-detection-model")

def detect_pothole(image_file):
    image = Image.open(image_file)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    predicted_class = outputs.logits.argmax(-1).item()
    print(f"Predicted class: {predicted_class}")
    return predicted_class


def assign_priority(predicted_class):
    if predicted_class == 1:
        return "Normal"
    return None


def send_email_to_admin(image_file,predicted_class):
    priority_label = assign_priority(predicted_class)

    latitude = 11.0611 
    longitude = 77.0346
    user_name = "Kishore Kumar S" 
    user_phone = "9043479026"
    admin_email = "kkishore51565@gmail.com"
    sender_email = "kishorekumars5643@gmail.com"  
    password = "dlku apwt kqhl eyxy" 
    category = "Pothole" if predicted_class == 1 else None
    subject = f"Complaint: Environmental Hazard Detected - {category}"
    
    body = f"""
    Dear Sir/Madam,

    I hope this message finds you well. I am writing to bring to your attention an environmental issue that has been detected in the vicinity. 
    This issue pertains to a {category} that poses a serious safety risk to the public and needs immediate attention.

    The attached image provides a clear view of the situation. It is crucial that this matter be addressed promptly to prevent any further accidents or complications. 
    As a responsible citizen, I urge you to prioritize the resolution of this environmental hazard.

    Priority: {priority_label}
    
    Location: You can view the location of the environmental hazard here: [ Location ](https://www.google.com/maps?q={latitude},{longitude})
    
    We look forward to your swift action in addressing this pressing concern.

    Thank you for your prompt attention to this matter.

    Sincerely,
    {user_name}  
    Phone: {user_phone}
    """

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = admin_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    img_byte_arr = BytesIO()
    image_file.seek(0)
    img_data = image_file.read() 
    img_byte_arr.write(img_data)
    img_byte_arr.seek(0)

    img_attachment = MIMEImage(img_byte_arr.read(), name="pothole_image.jpg")
    msg.attach(img_attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_email, password)
        server.sendmail(sender_email, admin_email, msg.as_string()) 
        server.quit() 
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")


