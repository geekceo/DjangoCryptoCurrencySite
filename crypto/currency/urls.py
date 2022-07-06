from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static
from currency.views import *

urlpatterns = [
    path('', index, name='home'),  #main page
    path('currencies/', currencyList, name='currencies'),
    path('currencies/<str:currencyId>/', currency, name='currency'),
    path('about/', currencyList, name='about')
]