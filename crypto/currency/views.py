from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from currency.models import CryptoCurrency
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
            'icons': dict(
                zip(
                    [icon.shortname for icon in CryptoCurrency.objects.all().order_by('id')],
                    [icon.iconpath for icon in [elem for elem in CryptoCurrency.objects.all().order_by('id')]]
            )),
            'stableCurrencyList': GET_STABLE_CURRENCY_LIST_PREVIEW(),
            'gamefiCurrencyList': GET_GAMEFI_CURRENCY_LIST_PREVIEW(),
            'currencyList': GET_CURRENCY_LIST_PREVIEW()
        })

def pageNotFound(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f"<h1>Страница не существует</h1>")