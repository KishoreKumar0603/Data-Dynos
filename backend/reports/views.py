from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import EnvironmentalIssue, PublicUser
from .serializers import EnvironmentalIssueSerializer


class EnvironmentalIssueCreateView(generics.CreateAPIView):
    queryset = EnvironmentalIssue.objects.all()
    serializer_class = EnvironmentalIssueSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """Custom save function to log and store data with user link."""
        user_id = self.request.data.get('user_id')
        try:
            user = PublicUser.objects.get(id=user_id)
            serializer.save(user=user)  # Link issue to logged-in user
            print("🔍 Received Data:", self.request.data)  # Debugging Log
        except PublicUser.DoesNotExist:
            return Response({"message": "Invalid user ID"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    """Registers a new user with hashed password."""
    if request.method == 'POST':
        username = request.data.get('username')
        aadhaar_number = request.data.get('aadhaar_number')
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        password = request.data.get('password')

        if not username or not aadhaar_number or not phone_number or not city or not password:
            return Response({"message": "All fields are required!"}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(password)

        try:
            user = PublicUser.objects.create(
                username=username,
                aadhaar_number=aadhaar_number,
                phone_number=phone_number,
                city=city,
                password=hashed_password
            )
            user.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from .models import PublicUser
from rest_framework import status

@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"message": "Username and password are required!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = PublicUser.objects.get(username=username)
        
        if check_password(password, user.password):  # Compare hashed password
            return Response({"message": "Login successful!", "username": user.username}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid password!"}, status=status.HTTP_401_UNAUTHORIZED)
    
    except PublicUser.DoesNotExist:
        return Response({"message": "User not found!"}, status=status.HTTP_404_NOT_FOUND)



import os
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
import numpy as np
from yolo_model import detect_potholes as dp
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage  # Import this
from django.core.files.base import ContentFile
from django.conf import settings

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        # Ensure 'uploads' directory exists inside MEDIA_ROOT
        upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Save the uploaded image inside media/uploads/
        image_path = os.path.join("uploads", image.name)
        saved_path = default_storage.save(image_path, ContentFile(image.read()))
        full_image_path = os.path.join(settings.MEDIA_ROOT, saved_path)  # Get absolute path

        # Verify file exists before proceeding
        if not os.path.exists(full_image_path):
            return JsonResponse({"error": "File not found after upload"}, status=500)

        # Run pothole detection
        with open(full_image_path, "rb") as img_file:
            predicted_class = dp.detect_pothole(img_file)

        # Send email if a pothole is detected
        if predicted_class == 1:
            with open(full_image_path, "rb") as img_file:
                dp.send_email_to_admin(img_file, predicted_class)

            return JsonResponse({"message": "Pothole detected! Email sent.", "prediction": predicted_class}, status=200)

        return JsonResponse({"message": "No pothole detected.", "prediction": predicted_class}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)
