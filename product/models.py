from django.db import models

# Create your models here.

# samsung or iphone
class Product(models.Model):
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    # throws an exception if you don't add number
    # of decimal places
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name
