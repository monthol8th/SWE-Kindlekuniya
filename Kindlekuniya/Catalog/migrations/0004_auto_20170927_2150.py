# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0003_auto_20170927_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalog.Product'),
        ),
    ]
