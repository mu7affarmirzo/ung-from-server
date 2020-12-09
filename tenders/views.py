from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from tenders.models import Tender, TenderLot, CompanyModel, FileTender
from tenders.serializers import (
    TenderSerializer,
    TenderLotSerializer,
    TenderCompaniesSerializer,
    TenderListSerializer,
    FileInfoSerializer,
    # CoTenSerializer,
    # CompaniesWithTenders
    )

class ApiTenderCompaniesListView(ListAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = TenderCompaniesSerializer
    
class TApiTenderCompaniesListView(ListAPIView):
    # queryset = CompanyModel.objects.all()
    serializer_class = TenderCompaniesSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        return CompanyModel.objects.filter(id=slug)

class ApiTenderLotsListView(ListAPIView):
    queryset = TenderLot.objects.all()
    serializer_class = TenderLotSerializer
    # pagination_class = PageNumberPagination

class ApiTendersListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    # pagination_class = PageNumberPagination

class CApiTendersListView(ListAPIView):
    serializer_class = TenderListSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        return Tender.objects.filter(company=slug)

class ApiTenderByListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderListSerializer
    pagination_class = PageNumberPagination

class FileInfoListViewAPI(ListAPIView):
    queryset = FileTender.objects.all()
    serializer_class = FileInfoSerializer

@api_view(['GET', ])
def api_detail_tenders_view(request, slug):
    try:
        news_tender = Tender.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TenderSerializer(news_tender)
        return Response(serializer.data)
