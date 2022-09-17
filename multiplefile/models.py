import os
from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
import datetime


def file_directory_path_instance(instance, filename, *args, **kwargs):
    return file_directory_path(filename)


def file_directory_path(filename, *args, **kwargs):
    return "/".join([datetime.datetime.today().strftime("%Y-%m-%d"), filename])


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class File(models.Model):
    file_id = models.AutoField(primary_key=True, verbose_name="File ID")
    upload_file = models.FileField(null=True,blank=True,upload_to=file_directory_path_instance,storage=OverwriteStorage(),verbose_name="Upload File",
    )
    upload_time = models.DateTimeField(verbose_name="Upload Time", auto_now=True)

