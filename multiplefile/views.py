from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (File, file_directory_path, )
from .serializers import FileSerializer
from rest_framework import viewsets


def file_upload(request):
    return render(request, "multiplefile/file.html")


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["post"])
    def multiple_files_upload(self, request, *args, **kwargs):
        files = request.FILES.getlist("files")
        for upload_file in files:
            try:
                obj = File.objects.get(
                    upload_file=file_directory_path(upload_file.name)
                )
                obj.upload_file = upload_file
                obj.save()
            except File.DoesNotExist:
                new_values = {"upload_file": upload_file}
                obj = File(**new_values)
                obj.save()
        return Response({"STATUS": "Multiple Files Uploaded"})
