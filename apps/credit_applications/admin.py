from django.contrib import admin

from apps.credit_applications.models import CreditApplication


@admin.register(CreditApplication)
class CreditApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "contract_id", "created_at")
    list_filter = ("contract_id",)
    search_fields = ("number",)
    list_display_links = ("id", "number")
