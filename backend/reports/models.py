from django.db import models

class EnvironmentalIssue(models.Model):
    CATEGORY_CHOICES = [
        ('deforestation', 'Deforestation'),
        ('plastic_pollution', 'Plastic Pollution'),
        ('illegal_dumping', 'Illegal Dumping'),
        ('oil_spill', 'Oil Spill'),
    ]

    image = models.ImageField(upload_to='reports/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} ({self.confidence_score}%)"
