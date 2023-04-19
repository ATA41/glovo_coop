from django.db import models


# Create your models here.
class Courier(models.Model):
    f_name = models.CharField(max_length=30)
    ph_number = models.CharField(max_length=13)


class Order(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name="orders")
