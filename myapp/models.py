from django.db import models
from myapp.specialfilefield import SpecialFileField
# Create your models here.

class VideoDetails(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = SpecialFileField(upload_to="myuploads/",length=600,max_upload_size=1073741824,content_types=["video/x-matroska","video/mp4"],)
    date_uploaded = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    