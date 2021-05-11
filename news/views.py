from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from news.models import UngNewsModel, RatingData
from news.serializers import (
    UngNewsSerializer, 
    UngNewsListSerializer, 
    SliderSerializer, 
    RatingsSerializer,

    UZnews,
    RUnews,
    ENnews,
    UZnewsspesific,
    RUnewsspesific,
    ENnewsspesific,
)

class RatingsListViewAPI(generics.ListAPIView):
    queryset = RatingData.objects.all()
    serializer_class = RatingsSerializer
    pagination_class = PageNumberPagination

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

class ApiNewsListView(generics.ListAPIView):
    queryset = UngNewsModel.objects.all()
    serializer_class = UngNewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)

# ************NEWS****************
@api_view(['GET', ])
def uz_detail_news_view(request, slug):
    try:
        news_post = UngNewsModel.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UZnewsspesific(news_post)
        return Response(serializer.data)

@api_view(['GET', ])
def ru_detail_news_view(request, slug):
    try:
        news_post = UngNewsModel.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RUnewsspesific(news_post)
        return Response(serializer.data)

@api_view(['GET', ])
def en_detail_news_view(request, slug):
    try:
        news_post = UngNewsModel.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ENnewsspesific(news_post)
        return Response(serializer.data)
class UZnews_list(generics.ListAPIView):
    queryset = UngNewsModel.objects.all()
    # x = {'temp': 'test'}
    serializer_class = UZnews
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)   
class RUnews_list(generics.ListAPIView):
    queryset = UngNewsModel.objects.all()
    # x = {'temp': 'test'}
    serializer_class = RUnews
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
class ENnews_list(generics.ListAPIView):
    queryset = UngNewsModel.objects.exclude(news_title=None)
    # x = {'temp': 'test'}
    serializer_class = ENnews
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)


class UZnews_list_allowed(generics.ListAPIView):
    # queryset = UngNewsModel.objects.all()
    serializer_class = UZnews
    

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.filter(mumkin_status=youth)   
class RUnews_list_allowed(generics.ListAPIView):
    serializer_class = RUnews

    def get_queryset(self):
        mum_status = self.kwargs['pk']
        return UngNewsModel.objects.filter(mumkin_status=mum_status)



class ENnews_list_allowed(generics.ListAPIView):
    serializer_class = ENnews

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.exclude(news_title=None).filter(mumkin_status=youth)

# **************NEWS END HERE***********


class SApiNewsListView(ListAPIView):
    serializer_class = SliderSerializer

    def get_queryset(self):
        slid = self.kwargs['pk']
        return UngNewsModel.objects.filter(status=slid)

#  ****************Youth union*******************

class UzYouthNewsListView(ListAPIView):
    serializer_class = UZnews

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.filter(youth_stat=youth, mumkin_status=youth)
class RuYouthNewsListView(ListAPIView):
    serializer_class = RUnews

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.filter(youth_stat=youth, mumkin_status=youth)
class EnYouthNewsListView(ListAPIView):
    serializer_class = ENnews

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.filter(youth_stat=youth, mumkin_status=youth)


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