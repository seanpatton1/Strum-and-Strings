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

    # ← Add this field
    price = models.DecimalField(
        max_digits=8,      # e.g. up to 999,999.99
        decimal_places=2,  # two decimal places for pence
        default=0.00,
        help_text="Price in GBP (e.g. 499.99)"
    )

    def __str__(self):
        return self.name
