from django.urls import URLPattern, path
from currency.views import *

urlpatterns = [
    path('', index),  #main page
    path('graphic/<str:currencyId>/', currency)
]