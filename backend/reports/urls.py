from django.urls import path
from .views import *

urlpatterns = [
    path('api/upload/', EnvironmentalIssueCreateView.as_view(), name='upload_issue'),
    path("accounts/register/", register, name="register"), 
    path("login/", login_user, name="login"),  # Ensure this path is correct
    path("upload-image/", upload_image, name="upload-image"),

]
