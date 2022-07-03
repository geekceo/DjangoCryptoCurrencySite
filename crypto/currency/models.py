from django.db import models

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=30)
    shortname = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    icon = models.ImageField('images/currency/')
    iconpath = models.CharField(max_length=96)

    def __str__(self) -> str:
        return f'{self.name}:{self.shortname}'