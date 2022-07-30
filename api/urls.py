from django.urls import path
import api.views as myapiview

urlpatterns = [
    
    # These Three are the urls that creates API ENDPOINTS
    path("videoslistsapi/<date>",myapiview.video_list, name="videolistview"),
    path("videouploadviewapi/",myapiview.VideoUploadView.as_view(),name="videouploadview"),
    path("checkpricingapi/",myapiview.CheckPricingView.as_view(),name="checkpricingview"),
    
]
