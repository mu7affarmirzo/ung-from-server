from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from news.views import (
    api_detail_news_view, ApiNewsListView, status_detail_news_view,
    # SliderViewset
    )


app_name = 'news'

# router = DefaultRouter()
# router.register('sliderstat', SliderViewset, basename='car-specs')

urlpatterns = [
    path('<slug>/', api_detail_news_view, name='detail'),
    path('list', ApiNewsListView.as_view(), name='list'),
    # path('slider/<status>', status_detail_news_view, name='sliders'),
    # url('', include(router.urls)),
    # path('slider', SliderViewset.as_view(), name='slider'),
]