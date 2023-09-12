from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    author = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()