from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    label = models.TextField(blank=True, default="")
    vendor_code = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    credit_application = models.ForeignKey(
        "credit_applications.CreditApplication",
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    manufacturer = models.ForeignKey(
        "organizations.Organization", related_name="products", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.id)
