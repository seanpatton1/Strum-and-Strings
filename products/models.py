from django.db import models
from django.templatetags.static import static
from cloudinary.models import CloudinaryField
from categories.models import Category


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    brand = models.CharField(
        max_length=100,
        help_text="e.g. Gibson, Martin, Yamaha, Fender, etc.",
        default="Unknown",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    model = models.CharField(
        max_length=100,
        help_text="e.g. Stratocaster, Les Paul, Dreadnought, etc."
    )
    image = CloudinaryField(
        "image",
        blank=True,
        null=True,
        help_text="Upload product image to Cloudinary."
    )
    short_description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        help_text="Price in GBP (e.g. 499.99)"
    )

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return static('images/placeholder.jpg')
