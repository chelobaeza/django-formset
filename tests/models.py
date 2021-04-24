from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
