from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
