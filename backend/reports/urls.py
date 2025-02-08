from django.urls import path
from .views import EnvironmentalIssueCreateView

urlpatterns = [
    path('upload/', EnvironmentalIssueCreateView.as_view(), name='upload_issue'),
]
