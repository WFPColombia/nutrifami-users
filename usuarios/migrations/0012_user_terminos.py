# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-13 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20171213_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='terminos',
            field=models.BooleanField(default=False, help_text='El usuario acept\xf3 t\xe9rminos y c\xf3ndiciones', verbose_name='T\xe9rminos y condiciones'),
        ),
    ]