from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', EnvironmentalIssueCreateView.as_view(), name='upload_issue'),
    path("accounts/register/", register, name="register"), 
    path("login/", login_user, name="login"),  # Ensure this path is correct

]
