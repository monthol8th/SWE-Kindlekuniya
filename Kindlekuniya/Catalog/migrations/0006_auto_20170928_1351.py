# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0005_auto_20170928_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
