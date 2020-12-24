from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Category, SubCategories, Documents, OffCategory, WithoutCategory

from .serializers import (
    CategorySerializer,
    SubCategoriesSerializer,
    DocumentsSerializer,
    FilterDocumentsSerializer,
    ChildsForNavbar,
    OffFilterDocumentsSerializer
)

class DocumentsCompaniesListViewAPi(ListAPIView):
    serializer_class = DocumentsSerializer

    def get_queryset(self):
        sub_c = self.kwargs['pk']
        return Documents.objects.filter(sub_catory=sub_c)
    pagination_class = PageNumberPagination


class AllDocCompaniesListViewAPi(ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    pagination_class = PageNumberPagination


class CategoriesCompaniesListViewAPi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

class ChildCategoriesCompaniesListViewAPi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ChildsForNavbar
    pagination_class = PageNumberPagination

class SubCategoriesFullCompaniesListViewAPi(ListAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    pagination_class = PageNumberPagination

    

class SubCategoriesListViewAPI(ListAPIView):
    serializer_class = SubCategoriesSerializer

    def get_queryset(self):
        slug = self.kwargs['pk']
        return SubCategories.objects.filter(category=slug)
    pagination_class = PageNumberPagination

class DocsSubCategoriesAPI(ListAPIView):
    serializer_class = FilterDocumentsSerializer

    def get_queryset(self):
        sub_c = self.kwargs['pk']
        return SubCategories.objects.filter(id=sub_c)
    pagination_class = PageNumberPagination

class OffDocsSubCategoriesAPI(ListAPIView):
    serializer_class = OffFilterDocumentsSerializer

    def get_queryset(self):
        sub_c = self.kwargs['pk']
        return OffCategory.objects.filter(id=sub_c)
    pagination_class = PageNumberPagination

class OffSubListViewAPi(ListAPIView):
    queryset = OffCategory.objects.all()
    serializer_class = OffFilterDocumentsSerializer