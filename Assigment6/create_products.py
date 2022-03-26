import os

import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_proj.settings")
django.setup()

from redis_cache.models import Product
for i in range(1000):
    Product.objects.create(name='phuong', description='VN', price= 101, date_created= timezone.now())