from django.shortcuts import render

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import ApplicationSerializer, QuestionaireSerializer, QuestionsSerializer

@api_view(['POST',])
def api_create_application_view(request):

    # account = request.user

    blog_post = ApplicationForm()

    if request.method == "POST":
        serializer = ApplicationSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionaireListView(generics.ListAPIView):
    queryset = QuestionaireModel.objects.all()
    serializer_class = QuestionsSerializer
    pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)


@api_view(['POST',])
def api_vote_icrement_view(request, id):

    try:
        question = QuestionaireModel.objects.get(id=id)
        print(question.options.get(id=2))
    except QuestionaireModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = QuestionaireSerializer(question, data=request.data)
        
        if serializer.is_valid():
            question.votes_count += 1
            question.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_option_icrement_view(request, id, sub_id):
    try:
        question = QuestionaireModel.objects.get(id=id)
        print(question)
        option = question.options.get(id=sub_id)
    except QuestionaireModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        serializer = QuestionsSerializer(question, data=request.data)

        if serializer.is_valid():
            option.votes += 1
            option.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)