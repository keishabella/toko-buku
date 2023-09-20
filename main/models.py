from django.db import models

class Product(models.Model):
    nama = models.CharField(max_length=255, default = "")
    kelas = models.TextField()
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)