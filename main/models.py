from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=255)
    kelas = models.TextField()
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()