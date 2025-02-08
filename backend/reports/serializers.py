from rest_framework import serializers
from .models import EnvironmentalIssue

class EnvironmentalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalIssue
        fields = '__all__'
