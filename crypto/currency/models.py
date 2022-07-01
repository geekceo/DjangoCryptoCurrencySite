from django.db import models

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30)
    shortname = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    icon = models.ImageField('images/currency/')

    def __str__(self) -> str:
        return self.name
