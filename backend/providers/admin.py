from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from providers.models import Product, Provider


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'date_launch', 'id')
    list_per_page = 20


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'country', 'city', 'debts', 'provider_link', 'id')
    list_per_page = 20
    list_filter = ('city', 'type')
    actions = ('clear_debts',)

    def clear_debts(self, request, queryset):
        for obj in queryset:
            obj.debts = 0
            obj.save()

    clear_debts.short_description = 'Очистить задолженность'

    def provider_link(self, obj):

        if obj.provider:
            link = reverse(
                'admin:providers_provider_change',
                args=(obj.provider.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.provider)
            )
