from django.db import models

class EnvironmentalIssue(models.Model):
    image = models.ImageField(upload_to="uploads/")
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False, default="11.061180")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False, default="77.034660")
    address = models.TextField(blank=False, null=False, default="Coimbatore")

    def __str__(self):
        return f"Environmental Issue - {self.id}"



# from django.db import models

# class EnvironmentalIssue(models.Model):
#     CATEGORY_CHOICES = [
#         ('deforestation', 'Deforestation'),
#         ('plastic_pollution', 'Plastic Pollution'),
#         ('illegal_dumping', 'Illegal Dumping'),
#         ('oil_spill', 'Oil Spill'),
#     ]

#     image = models.ImageField(upload_to='reports/')
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
#     confidence_score = models.FloatField(blank=True, null=True)
#     reported_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.category} ({self.confidence_score}%)"
