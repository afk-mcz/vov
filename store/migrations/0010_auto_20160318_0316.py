# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20160318_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.upload_image_to, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.upload_image_to, verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to=store.models.upload_image_to, verbose_name='Image'),
        ),
    ]
