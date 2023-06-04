from django.contrib import admin

from apps.organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "email", "owner", "created_at")
    list_filter = ("created_at", "code")
    search_fields = ("name", "code")
    list_display_links = ("id", "name")
