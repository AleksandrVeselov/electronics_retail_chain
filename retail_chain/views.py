from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from retail_chain.models import Link, Contacts


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


class ContactsListView(ListView):
    """Контроллер для отображения списка городов"""
    model = Contacts
    template_name = 'retail_chain/contacts-list.html'

    def get_queryset(self):

        contacts = Contacts.objects.all()
        queryset = []
        cities = []

        for contact in contacts:
            if contact.city not in cities:
                cities.append(contact.city)
                queryset.append(contact)

        return queryset
