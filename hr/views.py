from django.shortcuts import render
from rest_framework.generics import ListAPIView
from hr.models import *
from .serializers import *


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view





class CVListViewAPI(ListAPIView):
    queryset = UploadCv.objects.all()
    serializer_class = CVUploadsSerializers


@api_view(['POST', ])
# @permission_classes((IsAuthenticated,))
def cv_upload_view(request):

    account = request.user



    cv_uploader = UploadCv()

    if request.method == "POST":
        serializer = CVUploadsSerializers(cv_uploader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)