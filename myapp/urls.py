from django.urls import path

from myapp import views as myview


urlpatterns = [
    
    # These are urls for the backend of the application
    path("",myview.index,name="index"),
    
    path("list/",myview.show_list,name="videolist"),
    
    path("detailvideo/<id>",myview.show_detail,name="detailview"),
    
    path("pricing",myview.pricing_view,name="pricingview"),

]