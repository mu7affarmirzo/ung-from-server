from django.urls import path
from .views import *

app_name = 'hr'

urlpatterns = [
    path('list/', CVListViewAPI.as_view(), name='list'),
    path('list/try', cv_upload_view, name='try'),
]