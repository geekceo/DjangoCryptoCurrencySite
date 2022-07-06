from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from currency.models import CryptoCurrency, Category
from currency.config import *


def index(request) -> render:
    return render(request,
        'currency/index.html',
        {
            'title': 'Главная страница',
            'menu': MAIN_MENU
        })

def currency(request, currencyId) -> render:
    currency = get_object_or_404(CryptoCurrency, shortname=currencyId)

    return render(
        request,
        'currency/currency.html',
        { 
            'currencyId': currencyId,
            'menu': MAIN_MENU,
            'fullname': currency.name,
            'icon': currency.icon.url,
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