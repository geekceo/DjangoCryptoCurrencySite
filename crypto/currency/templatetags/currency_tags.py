import os
import requests
from django import template
from currency.models import *

register = template.Library()

@register.simple_tag()
def getCategory() -> set:
    return Category.objects.all()

@register.simple_tag(name='getValue')
def getDictValue(dictionary: dict, key: int | float| str) -> int | float | str | bool:
    return dictionary[key]

@register.simple_tag(name='allCurrencyPreview')
def getAllCurrencyListPreview() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')]
            )
        )

@register.simple_tag(name='allCurrency')
def getAllCurrencyList() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')]
            )
        )

@register.inclusion_tag('currency/inclusiontemps/currencyCategoriesList.html')
def showCurrenciesCategories() -> dict:
    allCurrencies = dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')]
            )
        )

    stableCurrencies = dict(
            zip(
                [x.name for x in CryptoCurrency.objects.filter(cat_id=1).order_by('id')][:3],
                [x.shortname for x in CryptoCurrency.objects.filter(cat_id=1).order_by('id')][:3]
                )
            )

    gamefiCurrencies = dict(
            zip(
                [x.name for x in CryptoCurrency.objects.filter(cat_id=2).order_by('id')][:3],
                [x.shortname for x in CryptoCurrency.objects.filter(cat_id=2).order_by('id')][:3]
                )
            )

    icons = dict(
                zip(
                    [icon.shortname for icon in CryptoCurrency.objects.all().order_by('id')],
                    [icon.icon.url for icon in [elem for elem in CryptoCurrency.objects.all().order_by('id')]]
                    )
                )

    return {'allCurrencies': allCurrencies, 'stableCurrencies': stableCurrencies, 'gamefiCurrencies': gamefiCurrencies, 'icons': icons}

@register.inclusion_tag('currency/inclusiontemps/currencyInfo.html')
def showCurrencyInfo(currencyId: str) -> dict:
    res = requests.get(f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={currencyId}&CMC_PRO_API_KEY={os.getenv("COINMARKETCAP_API_KEY")}').json()
    data = res['data'][currencyId][0]['quote']['USD']
    price = float(f"{float(data['price']):.2f}")
    cap = float(f"{float(data['market_cap']):.2f}")
    currencyInfo = {
            'Курс: ': f'${price:_}'.replace('_', ','),
            'Капитализация: ': f'${cap:_}'.replace('_', ','),
            'Изменение за 24 часа: ': f"{float(data['percent_change_24h']):.2f}%"
           }

    return {
            'name': CryptoCurrency.objects.get(shortname=currencyId).name, 'info': currencyInfo,
            'description':  CryptoCurrency.objects.get(shortname=currencyId).description
            }