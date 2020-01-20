from django.db import models
from shop.models import Product



# Create your models here.
class Checkout(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tampstamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title