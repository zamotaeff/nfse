from django.contrib import admin

from providers.models import Product, Provider


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'date_launch', 'id')
    list_per_page = 20


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'country', 'city', 'date_created', 'id')
    list_per_page = 20
