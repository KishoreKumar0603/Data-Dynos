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
