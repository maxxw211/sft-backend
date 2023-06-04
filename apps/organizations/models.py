import hashlib
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=128, blank=True, default="")
    code = models.CharField(max_length=64, blank=True, default="")
    email = models.EmailField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField("users.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = hashlib.sha1(self.email.encode("utf-8")).hexdigest()[:10]
        super().save(*args, **kwargs)
