# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-10 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20161110_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='photo',
            field=models.ImageField(default='not-found.jpg', upload_to='album/static/img'),
        ),
    ]
