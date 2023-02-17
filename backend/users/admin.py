from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "provider_link")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "password", "provider")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    def provider_link(self, obj):
        if obj.provider:
            link = reverse(
                'admin:providers_provider_change',
                args=(obj.provider.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.provider)
            )
