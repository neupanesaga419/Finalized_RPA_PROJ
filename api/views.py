from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from api.serializer import VideoDetailsSerializer,PricingSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from myapp.models import VideoDetails
from rest_framework.decorators import api_view

# This view will create API ENDPOINT for searching the videos uploaded with filter

@api_view(["GET"])
def video_list(request,date=None):
    if date is None:
        queryset = VideoDetails.objects.all()
        videolist =  VideoDetailsSerializer(queryset, many=True)
        return Response({"data":videolist.data})
    else:
        queryset = VideoDetails.objects.filter(date_uploaded=date)
        videolist =  VideoDetailsSerializer(queryset, many=True)
        return Response({"data":videolist.data})






# This view will create API Endpoint to recieve the video with proper validation
class VideoUploadView(APIView):
        
    def post(self,request,format=None):
        serializer = VideoDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Success",
                "data":serializer.data,
            })
        else:
            return Response({'serializer':serializer.errors})
            
      
#This view will create api endpoints for user to query about their price   
class CheckPricingView(APIView):
    def get(self,request,format=None):
            
        pricing = PricingSerializer()
        return Response({"serializer":"No Price"}) 
    
    def post(self,request,format=None):
        pricing = PricingSerializer(data= request.data)
        if pricing.is_valid():
            video_size = float(pricing.validated_data.get("video_size"))
            video_length = float(pricing.validated_data.get("video_length"))
            
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
            
            return Response({"data":charges})
        return Response({"serializer_error":pricing.errors})   