# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-16 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_auto_20180201_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Correo electr\xf3nico'),
        ),
    ]
