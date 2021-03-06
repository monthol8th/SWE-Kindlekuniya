# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-30 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0007_auto_20170929_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='histentry',
            name='status',
            field=models.CharField(choices=[('PROCESS', 'Processing'), ('TRANSIT', 'In Transit'), ('RECEIVE', 'Received')], default='PROCESS', max_length=7),
        ),
        migrations.AddField(
            model_name='histentry',
            name='trackingNo',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
    ]
