from rest_framework import serializers
from rest_framework.fields import IntegerField
from .models import File


class FileSerializer(serializers.ModelSerializer):
    file_id = IntegerField(required=False)

    class Meta:
        model = File
        fields = "__all__"
