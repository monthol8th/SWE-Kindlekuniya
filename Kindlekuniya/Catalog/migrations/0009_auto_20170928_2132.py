# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0008_auto_20170928_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagorymap',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='catagorymap',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.ManyToManyField(to='Catalog.Catagory'),
        ),
        migrations.DeleteModel(
            name='CatagoryMap',
        ),
    ]
