# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0005_auto_20171019_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
