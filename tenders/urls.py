from django.urls import path
from tenders.views import (
    # api_companies_tenders_view,
    api_detail_tenders_view, 
    ApiTendersListView, 
    ApiTenderLotsListView,
    ApiTenderCompaniesListView,
    ApiTenderByListView,
    
)

app_name = 'tenders'

urlpatterns = [
    path('list/<slug>', api_detail_tenders_view, name='detailed'),
    path('list/', ApiTenderByListView.as_view(), name='list'),
    path('list1', ApiTenderLotsListView.as_view(), name='list1'),

    path('companies', ApiTenderCompaniesListView.as_view(), name='list_companies'),
    # path('<name>/', api_companies_tenders_view, name='tender_by_companies'),

]