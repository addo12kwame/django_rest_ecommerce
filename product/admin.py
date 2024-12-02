from django.contrib.admin.sites import site
from .models import Product,ProductCategory
# Register your models here.

site.register(Product)
site.register(ProductCategory)
