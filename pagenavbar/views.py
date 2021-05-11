from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import MenuSubCategory, MenuCategories, ChildSubCategory

from .serializers import (
    CategoryMenuSerializer, 
    SubCategoryMenuSerializer, 
    MenuCatSerializer,
    ChildSerializer,
    ForChildSerializer,
    )

class MenuListAPI(ListAPIView):
    queryset = MenuCategories.objects.all()
    serializer_class = CategoryMenuSerializer


class MenuSubListAPI(ListAPIView):
    queryset = MenuSubCategory.objects.all()
    serializer_class = SubCategoryMenuSerializer

class NavbarAPI(ListAPIView):
    queryset = MenuCategories.objects.all()
    serializer_class = MenuCatSerializer

class ChildAPI(ListAPIView):
    queryset = ChildSubCategory.objects.all()
    serializer_class = ChildSerializer


class TestListAPI(ListAPIView):
    queryset = MenuSubCategory.objects.all()
    serializer_class = ForChildSerializer