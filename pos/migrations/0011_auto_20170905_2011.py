# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-05 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0010_auto_20170905_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_list',
            field=models.CharField(default='[]', max_length=10000),
        ),
    ]
