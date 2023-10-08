from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from retail_chain.models import Link, Contacts


class RetailChainView(LoginRequiredMixin, ListView):
    """Класс-контроллер для отображения главной страницы"""

    model = Link
    template_name = 'retail_chain/retail_chain.html'

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs.get('pk')
        queryset = Link.objects.all()
        if pk:
            city = Contacts.objects.get(pk=pk).city
            new_queryset = [link for link in queryset if link.contacts.city == city]
            queryset = new_queryset
        return queryset


class RetailChainDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения страницы с информацией о звене сети"""
    model = Link
    template_name = 'retail_chain/link_detail.html'


@login_required
def clear_debt(request, pk):
    """контроллер для обнуления задолженности перед поставщиком"""

    link = Link.objects.get(pk=pk)  # получаем нужное звено сети
    link.debt = 0  # обнуляем задолженность перед поставщиком
    link.save()  # сохраняем результат

    return redirect(reverse('retail-chain:retail-chain-list'))


class ContactsListView(LoginRequiredMixin, ListView):
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
