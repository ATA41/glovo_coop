from django.db import models

















class Order(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name="orders")
