from rest_framework import serializers
from django.template.defaultfilters import filesizeformat
from django.forms import forms
import moviepy.editor as mp



class SpecialSerializerField(serializers.FileField):
    
    def __init__(self,*args,**kwargs):
        
        # Extracting attribute values provided into SpecialFileField while creating Model
        
        self.content_types = kwargs.pop("content_types",[])
        self.max_upload_size = kwargs.pop("max_upload_size",0)
        self.length = kwargs.pop("length",0)
        super(SpecialSerializerField,self).__init__(*args,**kwargs)
    
    def to_internal_value(self,data):
        
        file = data
   
        try:
            print("into Try Field")
            # Getting content_type of the file user is
            my_content_type = file.content_type

            # Getting size of the file user is uploading
            file_size = file.size

            # Checking if the file content types matched with the content types initialized in
            # while creating Model
            
            if my_content_type in self.content_types:
                
                # Checking File Size 
                
                if file_size < self.max_upload_size:
                    # the temporary_file_path() function gives the path of file getting uploaded
                    # from user's interface
                    
                    file_path = file.temporary_file_path()
                    # VideoFileClip returns VideoFile from where we can extract details about
                    # a video file. 
                    
                    video = mp.VideoFileClip(file_path)
                    
                    # video.duration gives the duration of video in seconds
                    
                    duration = int(video.duration)

                    
                    if duration > self.length:
                        import time
                        
                        # This will convert time in  minutes from the time that have been provided in seconds
                        
                        max_duration = time.strftime("%M",time.gmtime(self.length))
                        
                        #This will convert time in hour minutes and seconds from the time
                        # that uploaded video contains
                        video_duration = time.strftime("%H:%M:%S",time.gmtime(duration))
                        
                        error = f"The video duration limit is only {max_duration} minutes.Your video duration is {video_duration}"
                        raise serializers.ValidationError((error))
                else:
                    raise serializers.ValidationError(("Please Upload File Under %s.Current FileSize is %s") %(filesizeformat(self.max_upload_size),
                                                                                                        filesizeformat(file_size)))

            else:
                raise serializers.ValidationError(("Unsupported File Types.Please Upload Video File of type mp4 and mkv"))
                            
                
                
            
        except AttributeError:
            pass
        
        return data  