from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
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
    )

class ApiTenderCompaniesListView(ListAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = TenderCompaniesSerializer

class ApiTenderLotsListView(ListAPIView):
    queryset = TenderLot.objects.all()
    serializer_class = TenderLotSerializer
    # pagination_class = PageNumberPagination

class ApiTendersListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    # pagination_class = PageNumberPagination


class ApiTenderByListView(ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderListSerializer


@api_view(['GET', ])
def api_detail_tenders_view(request, slug):
    try:
        news_tender = Tender.objects.get(slug=slug)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TenderSerializer(news_tender)
        return Response(serializer.data)

@api_view(['GET', ])
def api_companies_tenders_view(request, name):
    try:
        company_tender = CompanyModel.objects.get(name=name)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ApiTenderCompaniesListView(company_tender)
        return Response(serializer.data)
