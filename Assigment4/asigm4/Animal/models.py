from django.db import models

# Create your models here.

class Animal(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    color = models.CharField(max_length=50)
