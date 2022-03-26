from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=80)
    tel = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
        