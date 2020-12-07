from django.urls import path
from tenders.views import (
    # api_companies_tenders_view,
    api_detail_tenders_view, 
    ApiTendersListView, 
    CApiTendersListView,
    ApiTenderLotsListView,
    ApiTenderCompaniesListView,
    TApiTenderCompaniesListView,
    ApiTenderByListView,

    # CompaniesWithTendersListViewAPI,
)

app_name = 'tenders'

urlpatterns = [
    path('list/<slug>', api_detail_tenders_view, name='detailed'),
    path('list/', ApiTenderByListView.as_view(), name='list'),
    path('list/companies/<int:pk>', CApiTendersListView.as_view(), name='com_list'),
    path('list1', ApiTenderLotsListView.as_view(), name='list1'),
    path('companies', ApiTenderCompaniesListView.as_view(), name='list_companies'),
    path('companies/<int:pk>', TApiTenderCompaniesListView.as_view(), name='indiv_companies'),

    # path('compandtends/', CompaniesWithTendersListViewAPI.as_view(), name='companies_with_tenders'),
    # path('<int:id>/', api_companies_tenders_view, name='tender_by_companies'),

]