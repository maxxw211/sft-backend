from django.contrib import admin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "label",
        "vendor_code",
        "manufacturer",
        "credit_application_id",
        "created_at",
    )
    list_filter = ("title", "label", "vendor_code", "manufacturer")
    search_fields = ("title", "label", "vendor_code", "manufacturer")
    list_display_links = ("id", "vendor_code", "manufacturer", "credit_application_id")
