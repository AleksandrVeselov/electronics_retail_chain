from django.urls import path

from retail_chain.apps import RetailChainConfig
from retail_chain.views import RetailChainView, RetailChainDetailView, clear_debt, ContactsListView

app_name = RetailChainConfig.name

urlpatterns = [
    path('', RetailChainView.as_view(), name='retail-chain-list'),
    path('link/<int:pk>', RetailChainDetailView.as_view(), name='retail-chain'),
    path('clear-debt/<int:pk>', clear_debt, name='clear-debt'),
    path('city-list', ContactsListView.as_view(), name='city-list'),
]