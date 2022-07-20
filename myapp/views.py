from django.shortcuts import render,HttpResponseRedirect
from .forms import VideoForm,PricingForm,DateSearchForm
from .models import VideoDetails
import moviepy.editor as mp
from django.conf import settings
import mimetypes
from django.urls import reverse_lazy




# This view will handel the form for uploading videos
# If any error occurs it will show errors in template
# If form videoupload form doesnot have any errors then it will redirect to videolist

def index(request):
    fm = VideoForm()
    if request.method=="POST":
        fm = VideoForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse_lazy("videolist"))
    context = {"form":fm}
    return render(request,'index.html',context)


# This view will show all the videos that have been uploaded
# On Post request the view will show the videos uploaded on the user specified date
# It render a search form which takes date and filters the videos uploaded on specific date and returns it

def show_list(request):
    video_detail = None
    fm = DateSearchForm
    
    # if request.method == "GET":
    video_detail = VideoDetails.objects.all()
         
    if request.method == "POST":
        fm = DateSearchForm(request.POST)
        if fm.is_valid():
            date = fm.cleaned_data.get("date")
            video_detail = VideoDetails.objects.filter(date_uploaded = date)

    context = {"data":video_detail,"form":fm}
    
    return render(request,'list.html',context)

# This is show detail view which is triggered when user clicks on view full video button
# This show detail of video and get single video at a time.

def show_detail(request,id):
    template_name = "videodetails.html"
    
    details = None
    file_name = None
    
    if VideoDetails.objects.filter(id=id).exists():
        details = VideoDetails.objects.get(id=id)
        file_name = details.video_file.name.split("/")
        file_name = file_name[1]
    context = {"item":details,"file_name":file_name}
    return render(request, template_name,context)



# This view handels the query of the user about their charges on specified videos
# This view have a form with fields video_length , video_size and select field video_type
# The video_length must be provided in seconds and video size in MB both are number fields

def pricing_view(request):
    template_name = "pricing.html"
    fm = PricingForm
    charges = None
    if request.method =="POST":
        fm = PricingForm(request.POST)
        if fm.is_valid():
            video_size = fm.cleaned_data.get("video_size")
            video_length = fm.cleaned_data.get("video_length")
            video_type = fm.cleaned_data.get("video_type")
            
            if video_size < 500:
                if video_length < 378:
                    charges = "Your Charges is 17.5$"

                else:
                    charges = "Your Charges is 25$"
 
            else:
                if video_length < 378:
                    charges = "Your Charges is 25$"

                else:
                    charges = "Your Charges is 32.5$"

    context = {"form":fm,"charges":charges}
    return render(request,template_name,context)