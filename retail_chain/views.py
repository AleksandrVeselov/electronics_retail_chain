from django.shortcuts import render, redirect
from django.urls import reverse
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


def clear_debt(request, pk):
    """контроллер для обнуления задолженности перед поставщиком"""

    link = Link.objects.get(pk=pk)  # получаем нужное звено сети
    link.debt = 0  # обнуляем задолженность перед поставщиком
    link.save()  # сохраняем результат

    return redirect(reverse('retail-chain:retail-chain-list'))
