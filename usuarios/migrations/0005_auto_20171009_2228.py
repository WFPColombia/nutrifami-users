# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-09 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20171009_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ano_aprobacion',
        ),
        migrations.AddField(
            model_name='customuser',
            name='tipo_documento',
            field=models.CharField(choices=[('C\xe9dula de ciudadania', 'C\xe9dula de ciudadania'), ('C\xe9dula de extranjeria', 'C\xe9dula de extranjeria'), ('Tarjeta de identidad', 'Tarjeta de identidad'), ('Pasaporte', 'Pasaporte')], max_length=45, null=True, verbose_name='Tipos de documento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='codigo_beneficiario',
            field=models.PositiveIntegerField(blank=True, help_text='C\xf3digo asignado por el PMA a sus beneficiarios', null=True, verbose_name='c\xf3digo beneficiario'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='documento',
            field=models.PositiveIntegerField(blank=True, help_text='N\xfamero de documento de identidad del usuario', null=True, verbose_name='documento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='jefe_hogar',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Jefe de hogar'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='parentesco',
            field=models.CharField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Otro', 'Otro')], max_length=45, null=True, verbose_name='Parentesco'),
        ),
    ]