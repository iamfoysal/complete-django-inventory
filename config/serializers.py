from rest_framework import serializers
from .models import *

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

        




    
    
