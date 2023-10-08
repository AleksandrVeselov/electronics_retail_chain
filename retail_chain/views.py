from django.shortcuts import render
from django.views.generic import ListView, DetailView

from retail_chain.models import Link


class RetailChainView(ListView):
    """Класс-контроллер для отображения главной страницы"""

    model = Link
    template_name = 'retail_chain/retail_chain.html'


class RetailChainDetailView(DetailView):
    """Контроллер для отображения страницы с информацией о звене сети"""
    model = Link
    template_name = 'retail_chain/link_detail.html'
