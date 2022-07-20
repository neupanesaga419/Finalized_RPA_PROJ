
from django import forms
from .models import VideoDetails
from django.core.validators import MaxValueValidator,MinValueValidator


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoDetails
        fields = "__all__"
        
        labels = {
            "title":"Enter title of video",
            "description":"Enter Description of video",
            "video_file":"Upload Your File",
        }
        
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control p-2 m-2"}),
            "description":forms.Textarea(attrs={"class":"form-control p-2 m-2","cols":50,"rows":5}),
            "video_file":forms.FileInput(attrs={"class":"form-control p-2 m-2"}),
            
        }
 
class DateInput(forms.DateInput):
    input_type = 'date'
    
class DateSearchForm(forms.Form):
    date = forms.CharField(widget=DateInput(attrs={"class":"form-control"}),label="Select The Date")
     
    
    def __init__(self,*args,**kwargs):
        super(DateSearchForm,self).__init__(*args,**kwargs)
        for k,field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = "Please Select Date"
                

    
class PricingForm(forms.Form):
    video_choices = (("video/x-matroska","mkv"),("video/mp4","mp4"))
    video_size = forms.FloatField(
        label="Enter the size of video in MegaByte",
        widget=forms.NumberInput(attrs={"class":"form-control"}),
    )
    video_length = forms.FloatField(
        label="Enter Length of video in Seconds",
        widget=forms.NumberInput(attrs={"class":"form-control"}),
    )
    video_type = forms.ChoiceField(choices=video_choices,
                                   label="Select type of Video",
                                   widget=forms.Select(attrs={"class":"form-control"}))
    
    def clean_video_size(self):
        video_size = self.cleaned_data["video_size"]
        if video_size > 1024:
            raise forms.ValidationError("Please Enter Size Smaller than 1GB")

        if video_size < 0:
            raise forms.ValidationError("Enter Valid Size of Video")
        
        return video_size
    
    def clean_video_length(self):
        
        video_length = self.cleaned_data["video_length"]
        
        if video_length > 600:
            raise forms.ValidationError("Please Enter Video Length Smaller than 600 seconds")
        
        if video_length < 0:
            raise forms.ValidationError("Enter Valid Length of Video")
        
        return video_length