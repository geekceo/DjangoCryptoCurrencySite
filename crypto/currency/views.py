from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from currency.models import CryptoCurrency
from currency.config import MAIN_MENU, GET_CURRENCY_LIST, GET_CURRENCY_INFO


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
            'title': currencyId,
            'menu': MAIN_MENU,
            'fullname': CryptoCurrency.objects.get(shortname=currencyId).name,
            'info': GET_CURRENCY_INFO(currencyId=currencyId),
            'icon': CryptoCurrency.objects.get(shortname=currencyId).iconpath,
            'description':  CryptoCurrency.objects.get(shortname=currencyId).description
        })

def currencyList(request) -> render:
    return render(
        request,
        'currency/currencyList.html',
        { 
            'title': 'Криптовалюты',
            'menu': MAIN_MENU,
            'currencyList': GET_CURRENCY_LIST()
        })

def pageNotFound(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f"<h1>Страница не существует</h1>")