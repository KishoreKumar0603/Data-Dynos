from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from .models import EnvironmentalIssue
from .serializers import EnvironmentalIssueSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@method_decorator(csrf_exempt, name='dispatch')  # Temporarily disable CSRF for debugging
class EnvironmentalIssueCreateView(generics.CreateAPIView):
    queryset = EnvironmentalIssue.objects.all()
    serializer_class = EnvironmentalIssueSerializer
    parser_classes = (MultiPartParser, FormParser)

    def dispatch(self, request, *args, **kwargs):
        print(f"🔍 Received {request.method} request at {request.path}")  # Debugging log
        return super().dispatch(request, *args, **kwargs)
















# from django.shortcuts import render
# from rest_framework import generics
# from .models import EnvironmentalIssue
# from .serializers import EnvironmentalIssueSerializer
# from rest_framework.parsers import MultiPartParser, FormParser

# class EnvironmentalIssueCreateView(generics.CreateAPIView):
#     queryset = EnvironmentalIssue.objects.all()
#     serializer_class = EnvironmentalIssueSerializer
#     parser_classes = (MultiPartParser, FormParser)
