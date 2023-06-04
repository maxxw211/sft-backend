from django.contrib import admin

from apps.contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "number", "created_at")
    list_filter = ("number",)
    search_fields = ("number",)
    list_display_links = ("id",)
