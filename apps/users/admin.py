from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_owner",
        "is_active",
        "last_login",
    )
    list_editable = ("is_active", "is_owner")
    list_filter = ("is_active",)
    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("email",)
    list_display_links = ("email",)
