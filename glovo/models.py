from django.db import models

# Create your models here.
class Courier(models.Model):
    f_name = models.CharField(max_length=30)
    ph_number = models.CharField(max_length=13)
