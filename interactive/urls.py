from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'interactive'


urlpatterns = [
    path('application', api_create_application_view, name='application'),
    path('questionaire/', QuestionaireListView.as_view(), name='questionaire'),
    path('questionaire/<int:id>', api_vote_icrement_view, name='increment'),
    path('questionaire/<int:id>/<int:sub_id>', api_option_icrement_view, name='vote'),
]