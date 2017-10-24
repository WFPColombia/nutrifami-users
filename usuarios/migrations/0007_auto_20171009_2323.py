# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-09 23:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20171009_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
