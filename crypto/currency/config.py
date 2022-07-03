import os
import json
import requests
from currency.models import *

MAIN_MENU = {'Главная страница': '/', 'Криптовалюты': '/currencies', 'О сайте': '/about'}
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

def GET_CURRENCY_LIST() -> dict:
    return dict(
        zip(
            [x.name for x in CryptoCurrency.objects.all().order_by('id')],
            [x.shortname for x in CryptoCurrency.objects.all().order_by('id')]
            )
        )

def GET_CURRENCY_INFO(currencyId: str) -> dict:
    res = requests.get(f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={currencyId}&CMC_PRO_API_KEY={COINMARKETCAP_API_KEY}').json()
    data = res['data'][currencyId][0]['quote']['USD']
    return {
            'Курс: ': f"{float(data['price']):.2f} $",
            'Капитализация: ': f"{float(data['market_cap']):.2f} $",
            'Изменение за 24 часа: ': f"{float(data['percent_change_24h']):.2f} %"
           }
