from django.urls import path

from retail_chain.apps import RetailChainConfig
from retail_chain.views import (RetailChainView, RetailChainDetailView, clear_debt, ContactsListView, LinkListAPIView,
                                LinkCreateAPIView, LinkRetrieveAPIView, LinkDestroyAPIView, LinkUpdateAPIView)

app_name = RetailChainConfig.name

urlpatterns = [
    path('', RetailChainView.as_view(), name='retail-chain-list'),
    path('link/<int:pk>', RetailChainDetailView.as_view(), name='retail-chain'),
    path('clear-debt/<int:pk>', clear_debt, name='clear-debt'),
    path('city-list', ContactsListView.as_view(), name='city-list'),
    path('<int:pk>', RetailChainView.as_view(), name='retail-chain-city'),
    path('api/links', LinkListAPIView.as_view(), name='api-chain-list'),
    path('api/links/create', LinkCreateAPIView.as_view(), name='api-chain-create'),
    path('api/links/<int:pk>', LinkRetrieveAPIView.as_view(), name='api-chain'),
    path('api/links/delete/<int:pk>', LinkDestroyAPIView.as_view(), name='api-chain-destroy'),
    path('api/links/update/<int:pk>', LinkUpdateAPIView.as_view(), name='api-chain-update')

]