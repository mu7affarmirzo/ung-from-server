from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from tenders.models import Tender, TenderLot, CompanyModel
from tenders.serializers import (
    TenderSerializer,
    TenderLotSerializer,
    TenderCompaniesSerializer,
    TenderListSerializer,
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
    # queryset = Tender.objects.all()
    serializer_class = TenderListSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        return Tender.objects.filter(company=slug)

class ApiTenderByListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderListSerializer

# class CompaniesWithTendersListViewAPI(ListAPIView):
#     queryset = CompanyModel.objects.all()
#     serializer_class = CompaniesWithTenders

# class ApiTenderByListView(viewsets.ModelViewSet):
#     # queryset = Tender.objects.all()
#     serializer_class = TenderListSerializer(Tender, many = True)
#     def get_queryset(self):
#         company_tenders = Tender.objects.all()
#         return company_tenders

#     def retriever(self, request, *args, **kwargs):
#         params = kwargs
#         params_list = params['pk'].split('-')
#         tenders = Tender.objects.filter(
#             company_ten = params_list[0], car_model = params_list[1]
#         )
#         serializer = TenderListSerializer(tenders, many = True)
#         return Response(serializer.data)
    


@api_view(['GET', ])
def api_detail_tenders_view(request, slug):
    try:
        news_tender = Tender.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TenderSerializer(news_tender)
        return Response(serializer.data)

# @api_view(['GET', ])
# def api_companies_tenders_view(request, id):
#     try:
#         company_tender = CompanyModel.objects.get(id=id)

#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = CoTenSerializer(company_tender)
#         return Response(serializer.data)
