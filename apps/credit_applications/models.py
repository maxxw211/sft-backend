from django.db import models


class CreditApplication(models.Model):
    number = models.CharField(unique=True)
    contract = models.ForeignKey(
        "contracts.Contract",
        related_name="credit_application",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)
