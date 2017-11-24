# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20171124_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='id',
        ),
        migrations.AlterField(
            model_name='collections',
            name='collection_name',
            field=models.CharField(blank=True, max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='collection'),
        ),
    ]
