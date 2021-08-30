import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from itertools import chain

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from django.core.mail import send_mail


from django.db.models import Q


from news.models import *
from tenders.models import Tender
from news.serializers import *

class ComplianceApiNewsListView(generics.ListAPIView):
    queryset = ComplNewsModel.objects.all()
    serializer_class = ComplianceNewsListSerializer
    pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['news_title', 'news_body']


@api_view(['GET',])
def complinace_news_detail(request, slug):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ComplNewsModel.objects.get(slug=slug)
    except ComplNewsModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComplianceNewsSerializer(snippet)
        return Response(serializer.data)


class RatingsListViewAPI(generics.ListAPIView):
    queryset = RatingData.objects.all()
    serializer_class = RatingsSerializer
    pagination_class = PageNumberPagination

@api_view(['GET', ])
def api_detail_news_view(request, slug):

    send_mail(
        'HEllo',
        'This is email test',
        'cmuzaffarmirzo@gmail.com',
        ['m.choriev@student.inha.uz', 'm.choriev@ung.uz '],
        fail_silently=False,
    )

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
    # filter_backends = (SearchFilter, OrderingFilter)
    filter_backends = [filters.SearchFilter]
    search_fields = ['news_title', 'news_body']

class SApiNewsListView(ListAPIView):
    serializer_class = SliderSerializer

    def get_queryset(self):
        slid = self.kwargs['pk']
        return UngNewsModel.objects.filter(status=slid)

class YApiNewsListView(ListAPIView):
    serializer_class = SliderSerializer

    def get_queryset(self):
        youth = self.kwargs['pk']
        return UngNewsModel.objects.filter(youth_stat=youth)


class SliderViewset(viewsets.ModelViewSet):
    serializer_class = SliderSerializer

    def get_queryset(self):
        stat = UngNewsModel.objects.all()
        return stat

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        truuue = UngNewsModel.objects.filter(stat_type=params['pk'])
        serializer = SliderSerializer(truuue, many=True)
        return Response(serializer.data)



def get_news_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = UngNewsModel.filter(
            Q(news_title__icontrains=q) |
            Q(news_body__icontrains=q)).distinct()
        for post in posts:
            queryset.append(post)

    return list(set(queryset))

@api_view(['POST', ])
def search(request):

    a = request.data.dict()['word']
    print(type(request.data))
    print(request.data['word'])
    if request.method == 'POST':
        queryset_news = UngNewsModel.objects.filter(
            Q(news_title_uz__contains=a) | 
            Q(news_title_ru__contains=a) | 
            Q(news_title_en__contains=a))

        queryset_tenders = Tender.objects.filter(
            Q(title_uz__contains=a) | 
            Q(title_ru__contains=a) | 
            Q(title_en__contains=a))

        serializer_news = SeachNewsSerializer(queryset_news, many=True)
        serializer_tenders = SeachTendersSerializer(queryset_tenders, many=True)
        new_data = serializer_news.data + serializer_tenders.data

        return Response(new_data)


