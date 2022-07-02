from currency.models import *

CURRENCY_PARAMS = ['Курс: ', 'Капитализация: ', 'Процент роста: ']
MAIN_MENU = {'Главная страница': '/', 'Криптовалюты': '/currencies', 'О сайте': '/about'}

def GET_CURRENCY_LIST() -> dict:
    names = [x.name for x in CryptoCurrency.objects.all()]
    shortnames = [x.shortname for x in CryptoCurrency.objects.all()]
    return dict(zip(names, shortnames))