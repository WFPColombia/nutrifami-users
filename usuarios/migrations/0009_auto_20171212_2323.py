# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-12 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_avance_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='Correo electr\xf3nico'),
        ),
    ]
