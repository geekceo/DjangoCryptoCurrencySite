import os
import json
import requests
from currency.models import *

MAIN_MENU = {'Главная страница': 'home', 'Криптовалюты': 'currencies', 'О сайте': 'about'}
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

def GET_CURRENCY_LIST() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.all().order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.all().order_by('id')]
            )
        )

def GET_CURRENCY_LIST_PREVIEW() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(pk__lte=3).order_by('id')]
            )
        )

def GET_STABLE_CURRENCY_LIST_PREVIEW() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(cat_id=1).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(cat_id=1).order_by('id')]
            )
        )

def GET_GAMEFI_CURRENCY_LIST_PREVIEW() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.filter(cat_id=2).filter(pk__gte=3).order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.filter(cat_id=2).filter(pk__gte=3).order_by('id')]
            )
        )

def GET_CURRENCY_INFO(currencyId: str) -> dict:
    res = requests.get(f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={currencyId}&CMC_PRO_API_KEY={COINMARKETCAP_API_KEY}').json()
    data = res['data'][currencyId][0]['quote']['USD']
    price = float(f"{float(data['price']):.2f}")
    cap = float(f"{float(data['market_cap']):.2f}")
    return {
            'Курс: ': f'${price:_}'.replace('_', ','),
            'Капитализация: ': f'${cap:_}'.replace('_', ','),
            'Изменение за 24 часа: ': f"{float(data['percent_change_24h']):.2f}%"
           }
