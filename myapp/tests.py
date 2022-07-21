from django.test import TestCase

# Create your tests here.
# class VideoDetailView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "myvideodetails.html"
    
#     def get(self,request,pk):
#         video = get_object_or_404(VideoDetails, pk=pk)
#         serializer = VideoDetailsSerializer(video)
#         return Response({'serializer':serializer,'video':video})
    
#     def post(self,request,pk):
        
    
#         video = get_object_or_404(VideoDetails,pk=pk)
#         serializer = VideoDetailsSerializer(video,data=request.data)
        
#         if not serializer.is_valid():
#             return Response({'serializer':serializer,'video':video})
        
#         serializer.save()
#         return redirect('videolistview')
