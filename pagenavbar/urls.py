from django.urls import path
from .views import (
    MenuListAPI, 
    MenuSubListAPI,
    NavbarAPI,
)

app_name = 'pagenavbar'

urlpatterns = [
    path('categories/', MenuListAPI.as_view(), name='menu'),
    path('navbar/', NavbarAPI.as_view(), name='navbar'),
    path('subcategories/', MenuSubListAPI.as_view(), name='submenu'),
]