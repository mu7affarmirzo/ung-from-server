from django.urls import path
from .views import (
    MenuListAPI, 
    MenuSubListAPI,
    NavbarAPI,
    ChildAPI,
    TestListAPI
)

app_name = 'pagenavbar'

urlpatterns = [
    path('categories/', MenuListAPI.as_view(), name='menu'),
    path('navbar/', NavbarAPI.as_view(), name='navbar'),
    path('subcategories/', MenuSubListAPI.as_view(), name='submenu'),
    path('child/', ChildAPI.as_view(), name='child'),
    path('test/', TestListAPI.as_view(), name='test'),
]