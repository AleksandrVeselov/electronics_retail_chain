from django.urls import path

from retail_chain.apps import RetailChainConfig
from retail_chain.views import RetailChainView

app_name = RetailChainConfig.name

urlpatterns = [
    path('', RetailChainView.as_view(), name='retail-chain'),
]