# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-14 16:58
from __future__ import unicode_literals

import adminsortable.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20170914_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order', 'date', 'sku'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'ordering': ['order', 'date'], 'verbose_name': 'Product Variant Image', 'verbose_name_plural': 'Product Variant Images'},
        ),
        migrations.AlterModelOptions(
            name='productvariant',
            options={'ordering': ['order', 'product'], 'verbose_name': 'Product Variant', 'verbose_name_plural': 'Product Variants'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
    ]
