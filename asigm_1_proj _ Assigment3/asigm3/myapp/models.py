from django.db import models

# Create your models here.
class Person(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null= True)

class Manufacturer(models.Model):
    manufacturer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

