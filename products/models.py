from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    model = models.CharField(
        max_length=100,
        help_text="e.g. Stratocaster, Les Paul, Dreadnought, etc."
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )
    short_description = models.TextField(blank=True)

    def __str__(self):
        return self.name
