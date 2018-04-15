from django.db import models
from decimal import Decimal

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    ship_address = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    total_price = models.FloatField()
    name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    cart_code = models.DecimalField(decimal_places=3, max_digits=10)
    total_price = 	models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField()

    def __str__(self):
        return self.title