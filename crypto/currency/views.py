from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request) -> HttpResponse:
    return HttpResponse("Главная страница")

def currency(request, currencyId) -> HttpResponse:
    return HttpResponse(f"Валюта: {currencyId}")

def pageNotFound(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(f"<h1>Страница не существует</h1>")