from rest_framework import serializers
from myapp.models import *
from myapp.specialserializer import SpecialSerializerField

class VideoDetailsSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=2000)
    video_file = SpecialSerializerField(length=600,max_upload_size=1073741824,content_types=["video/x-matroska","video/mp4"])

    def create(self,validated_data):
        return VideoDetails.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.video_file = validated_data.get('video_file',instance.video_file)
        instance.save()
        return instance
    

class TimeFilterSerializer(serializers.Serializer):
    search_date = serializers.DateField()
    

   
class PricingSerializer(serializers.Serializer):
    video_choices = (("video/x-matroska","mkv"),("video/mp4","mp4"))
    video_size = serializers.FloatField(
        label="Enter the size of video in MegaByte",

    )
    video_length = serializers.FloatField(
        label="Enter Length of video in Seconds",
    )
    video_type = serializers.ChoiceField(choices=video_choices,
                                   label="Select type of Video",)
    
    def validate_video_size(self,data):
        video_size = data
        if video_size > 1024:
            raise serializers.ValidationError("Please Enter Size Smaller than 1GB")

        if video_size < 0:
            raise serializers.ValidationError("Enter Valid Size of Video")
        
        return video_size
    
    def validate_video_length(self,data):
        
        video_length = data
        
        if video_length > 600:
            raise serializers.ValidationError("Please Enter Video Length Smaller than 600 seconds")
        
        if video_length < 0:
            raise serializers.ValidationError("Enter Valid Length of Video")
        
        return video_length