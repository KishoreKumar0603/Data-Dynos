from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', EnvironmentalIssueCreateView.as_view(), name='upload_issue'),
    path("accounts/register/", register, name="register"), 

]
