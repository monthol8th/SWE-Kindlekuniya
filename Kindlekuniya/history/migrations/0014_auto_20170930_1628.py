# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_auto_20170928_2132'),
        ('history', '0013_auto_20170930_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histdata',
            name='orderName',
        ),
        migrations.AddField(
            model_name='histdata',
            name='productID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Catalog.Product'),
        ),
    ]
