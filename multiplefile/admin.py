from django.contrib import admin
from .models import File

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'upload_file', 'upload_time')

admin.site.register(File, FileAdmin)
