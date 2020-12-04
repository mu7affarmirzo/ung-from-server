from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from news.models import UngNewsModel
from news.serializers import UngNewsSerializer, UngNewsListSerializer

@api_view(['GET', ])
def api_detail_news_view(request, slug):
    try:
        news_post = UngNewsModel.objects.get(slug=slug)

    except UngNewsSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UngNewsSerializer(news_post)
        return Response(serializer.data)

class ApiNewsListView(ListAPIView):
    queryset = UngNewsModel.objects.all()
    serializer_class = UngNewsListSerializer
    pagination_class = PageNumberPagination
