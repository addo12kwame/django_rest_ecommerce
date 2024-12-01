from django.contrib.admin.sites import site
from .models import Product
# Register your models here.

site.register(Product)