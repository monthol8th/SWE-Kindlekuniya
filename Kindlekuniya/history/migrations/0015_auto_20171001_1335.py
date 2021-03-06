# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20170930_1652'),
        ('history', '0014_auto_20170930_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='histentry',
            name='orderOwner',
        ),
        migrations.AddField(
            model_name='histentry',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Address'),
        ),
        migrations.AddField(
            model_name='histentry',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
