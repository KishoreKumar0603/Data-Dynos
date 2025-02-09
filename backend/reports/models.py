from django.db import models

class EnvironmentalIssue(models.Model):
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False, default="11.061180")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False, default="77.034660")
    address = models.TextField(blank=False, null=False, default="Coimbatore")

    def __str__(self):
        return f"Environmental Issue - {self.id}"


class PublicUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    aadhaar_number = models.CharField(max_length=12, unique=True)  # Aadhaar numbers are 12 digits
    phone_number = models.CharField(max_length=15)  # Depending on your validation needs, you may adjust the length
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Store the hashed password
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the user was created

    def __str__(self):
        return self.username
