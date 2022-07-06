from django.contrib import admin
from .models import *

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shortname', 'description', 'cat')
    list_display_links = ('name',)
    search_fields = ('description', 'name')
    list_editable = ('shortname',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(CryptoCurrency, CurrencyAdmin)
admin.site.register(Category, CategoryAdmin)
