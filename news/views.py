from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView

from news.models import UngNewsModel
from news.serializers import UngNewsSerializer, UngNewsListSerializer, SliderSerializer

@api_view(['GET', ])
def api_detail_news_view(request, slug):
    try:
        news_post = UngNewsModel.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UngNewsSerializer(news_post)
        return Response(serializer.data)

@api_view(['GET', ])
def status_detail_news_view(request, status):
    try:
        news_post = UngNewsModel.objects.get(status=status)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UngNewsSerializer(news_post)
        return Response(serializer.data)

class ApiNewsListView(ListAPIView):
    queryset = UngNewsModel.objects.all()
    serializer_class = UngNewsSerializer
    pagination_class = PageNumberPagination

class SApiNewsListView(ListAPIView):
    serializer_class = UngNewsSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        return UngNewsModel.objects.filter(slider_status=slug)


# class StatusApiNewsListView(ListAPIView):
#     # queryset = UngNewsModel.objects.all()
#     serializer_class = UngNewsSerializer

#     def get_queryset(self):
#         slider = self.request
    

class SliderViewset(viewsets.ModelViewSet):
    serializer_class = SliderSerializer

    def get_queryset(self):
        stat = UngNewsModel.objects.all()
        return stat

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        truuue = UngNewsModel.objects.filter(stat_type=params['pk'])
        serializer = CarSpecsSerializer(truuue, many=True)
        return Response(serializer.data)