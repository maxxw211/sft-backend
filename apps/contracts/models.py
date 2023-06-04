from django.core.validators import MinValueValidator
from django.db import models


class Contract(models.Model):
    text = models.TextField(blank=True, null=True)
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)
