from django.contrib.sitemaps import Sitemap
from products.models import Product


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return f'/products/{item.id}/'
