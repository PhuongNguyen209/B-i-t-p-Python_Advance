# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2022-02-28 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asigm_1_app', '0003_auto_20220228_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]
