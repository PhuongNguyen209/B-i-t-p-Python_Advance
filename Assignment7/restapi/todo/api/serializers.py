from rest_framework import serializers
from todo.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'age', 'address', 'tel', 'timestamp', 'updated','completed', 'user']