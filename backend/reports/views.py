from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import EnvironmentalIssue
from .serializers import EnvironmentalIssueSerializer

class EnvironmentalIssueCreateView(generics.CreateAPIView):
    queryset = EnvironmentalIssue.objects.all()
    serializer_class = EnvironmentalIssueSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """Custom save function to log and store data."""
        print("🔍 Received Data:", self.request.data)  # Debugging Log
        serializer.save()


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PublicUser
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        aadhaar_number = request.data.get('aadhaar_number')
        phone_number = request.data.get('phone_number')
        city = request.data.get('city')
        password = request.data.get('password')

        if not username or not aadhaar_number or not phone_number or not city or not password:
            return Response({"message": "All fields are required!"}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password before storing it in the database
        hashed_password = make_password(password)

        try:
            # Create a new PublicUser instance
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














# from django.shortcuts import render
# from rest_framework import generics
# from .models import EnvironmentalIssue
# from .serializers import EnvironmentalIssueSerializer
# from rest_framework.parsers import MultiPartParser, FormParser

# class EnvironmentalIssueCreateView(generics.CreateAPIView):
#     queryset = EnvironmentalIssue.objects.all()
#     serializer_class = EnvironmentalIssueSerializer
#     parser_classes = (MultiPartParser, FormParser)
