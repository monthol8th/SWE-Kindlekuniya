# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('isMonocrome', models.BinaryField()),
                ('paperType', models.CharField(max_length=30)),
                ('coverType', models.CharField(max_length=30)),
                ('page', models.IntegerField()),
                ('size', models.CharField(max_length=30)),
                ('discription', models.CharField(max_length=240)),
                ('pictureUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Product')),
            ],
        ),
    ]
