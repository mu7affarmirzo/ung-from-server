from django.urls import path
from .views import (
    DocumentsCompaniesListViewAPi,
    AllDocCompaniesListViewAPi,
    CategoriesCompaniesListViewAPi,
    SubCategoriesListViewAPI,
    SubCategoriesFullCompaniesListViewAPi,
    DocsSubCategoriesAPI,
    ChildCategoriesCompaniesListViewAPi,
    OffDocsSubCategoriesAPI,
    OffSubListViewAPi,
)

app_name = 'ungfiles'

urlpatterns = [
    path('docs/<int:pk>', DocumentsCompaniesListViewAPi.as_view(), name='docs'),
    path('docs/', AllDocCompaniesListViewAPi.as_view(), name='alldocs'),
    path('categories/', CategoriesCompaniesListViewAPi.as_view(), name='categories'),
    path('categories/<int:pk>', SubCategoriesListViewAPI.as_view(), name='sub_categories'),
    path('categories/sub', SubCategoriesFullCompaniesListViewAPi.as_view(), name='sub'),
    path('categories/sub/<int:pk>', DocsSubCategoriesAPI.as_view(), name='sub_docs'),
    path('offsub', OffSubListViewAPi.as_view(), name='off'),
    path('offsub/<int:pk>', OffDocsSubCategoriesAPI.as_view(), name='off_docs'),

    path('child/', ChildCategoriesCompaniesListViewAPi.as_view(), name='childs'),
]
