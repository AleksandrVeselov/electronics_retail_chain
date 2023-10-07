from django.urls import path

from retail_chain.apps import RetailChainConfig

app_name = RetailChainConfig.name

urlpatterns = [
    path('', RetailChainView.as_view(), name='retail-chain'),
]