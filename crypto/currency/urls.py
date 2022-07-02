from django.urls import URLPattern, path
from currency.views import *

urlpatterns = [
    path('', index),  #main page
    path('currencies/', currencyList),
    path('currencies/<str:currencyId>/', currency)
]