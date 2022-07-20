from django.contrib import admin
from .models import VideoDetails
# Register your models here.
@admin.register(VideoDetails)
class VideoDetailsAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","video_file","date_uploaded"]
    