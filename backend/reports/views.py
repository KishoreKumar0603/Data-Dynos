from django.shortcuts import render
from rest_framework import generics
from .models import EnvironmentalIssue
from .serializers import EnvironmentalIssueSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class EnvironmentalIssueCreateView(generics.CreateAPIView):
    queryset = EnvironmentalIssue.objects.all()
    serializer_class = EnvironmentalIssueSerializer
    parser_classes = (MultiPartParser, FormParser)
