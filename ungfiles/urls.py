from django.urls import path
from .views import (
    DocumentsCompaniesListViewAPi,
    CategoriesCompaniesListViewAPi,
    SubCategoriesListViewAPI,
    SubCategoriesFullCompaniesListViewAPi,
    DocsSubCategoriesAPI,
)

app_name = 'ungfiles'

urlpatterns = [
    path('docs/', DocumentsCompaniesListViewAPi.as_view(), name='docs'),
    path('categories/', CategoriesCompaniesListViewAPi.as_view(), name='categories'),
    path('categories/<int:pk>', SubCategoriesListViewAPI.as_view(), name='sub_categories'),
    path('categories/sub', SubCategoriesFullCompaniesListViewAPi.as_view(), name='sub'),
    path('categories/sub/<int:pk>', DocsSubCategoriesAPI.as_view(), name='sub_docs'),
]
