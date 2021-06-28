from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from news.views import (
    api_detail_news_view, ApiNewsListView, status_detail_news_view,
    SApiNewsListView,
    YApiNewsListView,
    RatingsListViewAPI,
    search,
    )

app_name = 'news'


urlpatterns = [
    path('<slug>/', api_detail_news_view, name='detail'),
    path('list', ApiNewsListView.as_view(), name='list'),
    path('search', search, name='search'),
    path('ratings', RatingsListViewAPI.as_view(), name='ratings'),
    path('slider/<int:pk>', SApiNewsListView.as_view(), name='slider_list'),
    path('youth/<int:pk>', YApiNewsListView.as_view(), name='youth_list'),

]