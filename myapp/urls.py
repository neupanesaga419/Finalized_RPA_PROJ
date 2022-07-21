from django.urls import path

from myapp import views as myview


urlpatterns = [
    
    path("",myview.index,name="index"),
    
    path("list/",myview.show_list,name="videolist"),
    
    path("detailvideo/<id>",myview.show_detail,name="detailview"),
    
    path("pricing",myview.pricing_view,name="pricingview"),


    # These Three are the urls that creates API ENDPOINTS
    
    path("videoslistsapi/",myview.VideoListView.as_view(),name="videolistview"),
    path("videouploadviewapi/",myview.VideoUploadView.as_view(),name="videouploadview"),
    path("checkpricingapi/",myview.CheckPricingView.as_view(),name="checkpricingview"),
    
    
]