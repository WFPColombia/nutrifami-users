# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-13 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_auto_20180530_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('C\xe9dula de ciudadania', 'C\xe9dula de ciudadania'), ('Otro', 'Otro'), ('Pasaporte', 'Pasaporte')], max_length=45, null=True, verbose_name='Tipo de usuario'),
        ),
    ]