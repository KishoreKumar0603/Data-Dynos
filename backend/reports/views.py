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
















# from django.shortcuts import render
# from rest_framework import generics
# from .models import EnvironmentalIssue
# from .serializers import EnvironmentalIssueSerializer
# from rest_framework.parsers import MultiPartParser, FormParser

# class EnvironmentalIssueCreateView(generics.CreateAPIView):
#     queryset = EnvironmentalIssue.objects.all()
#     serializer_class = EnvironmentalIssueSerializer
#     parser_classes = (MultiPartParser, FormParser)
