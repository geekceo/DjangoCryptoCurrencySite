from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from currency.models import CryptoCurrency, Category
from currency.config import *


def index(request) -> render:
    return render(request,
        'currency/index.html',
        {
            'title': 'Страница',
            'menu': MAIN_MENU
        })

def currency(request, currencyId) -> render:
    return render(
        request,
        'currency/currency.html',
        { 
            'currencyId': currencyId,
            'menu': MAIN_MENU,
            'fullname': CryptoCurrency.objects.get(shortname=currencyId).name,
            'icon': CryptoCurrency.objects.get(shortname=currencyId).icon.url,
        })

def currencyList(request) -> render:
    return render(
        request,
        'currency/currencyList.html',
        { 
            'title': 'Криптовалюты',
            'menu': MAIN_MENU
        })

def pageNotFound(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f"<h1>Страница не существует</h1>")