from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from news.views import *
# (
#     api_detail_news_view, ApiNewsListView, status_detail_news_view,
#     SApiNewsListView,
#     YApiNewsListView,
#     RatingsListViewAPI,
    
#     UZnews_list,
#     RUnews_list,
#     ENnews_list,
#     uz_detail_news_view,
#     ru_detail_news_view,
#     en_detail_news_view
#     )

app_name = 'news'


urlpatterns = [
    path('<slug>/', api_detail_news_view, name='detail'),
    path('list', ApiNewsListView.as_view(), name='list'),
    path('ratings', RatingsListViewAPI.as_view(), name='ratings'),
    path('slider/<int:pk>', SApiNewsListView.as_view(), name='slider_list'),


    path('uzyouth/<int:pk>', UzYouthNewsListView.as_view(), name='uzyouth_list'),
    path('ruyouth/<int:pk>', RuYouthNewsListView.as_view(), name='ruyouth_list'),
    path('enyouth/<int:pk>', EnYouthNewsListView.as_view(), name='enyouth_list'),


    path('uzlist', UZnews_list.as_view(), name='uzlist'),
    path('uzallowed/<int:pk>', UZnews_list_allowed.as_view(), name='uzallowed'),
    path('uz/<slug>/', uz_detail_news_view, name='uzdetail'),

    path('rulist', RUnews_list.as_view(), name='rulist'),
    # path('ruallowed', RUnews_list.as_view(), name='ruallowed'),
    path('ru/<slug>/', ru_detail_news_view, name='rudetail'),
    path('rual/<int:pk>', RUnews_list_allowed.as_view(), name='rual'),

    path('enlist', ENnews_list.as_view(), name='enlist'),
    path('enallowed/<int:pk>', ENnews_list_allowed.as_view(), name='enallowed'),
    path('en/<slug>/', en_detail_news_view, name='endetail'),

]