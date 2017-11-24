# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-24 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(blank=True, max_length=32, unique=True, verbose_name='collection')),
                ('collection_description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('collection_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('collection_title_img', models.ImageField(blank=True, upload_to='media', verbose_name='title_img')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(blank=True, max_length=32, unique=True, verbose_name='collection')),
                ('img_img', models.ImageField(blank=True, upload_to='media', verbose_name='img')),
                ('collection_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Collections')),
            ],
        ),
    ]
