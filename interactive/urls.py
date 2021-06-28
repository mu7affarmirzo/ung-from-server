from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'interactive'


urlpatterns = [
    path('application', api_create_application_view, name='application'),
]