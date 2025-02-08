from django.urls import path
from .views import z

urlpatterns = [
    path('upload/', EnvironmentalIssueCreateView.as_view(), name='upload_issue'),
]
