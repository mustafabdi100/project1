# your_app/admin.py

from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name',)
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
