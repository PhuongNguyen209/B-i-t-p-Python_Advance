from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    def __str__(self):
        return self.name