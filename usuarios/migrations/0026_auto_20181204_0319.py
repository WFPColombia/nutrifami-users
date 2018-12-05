# Generated by Django 2.1.4 on 2018-12-04 03:19

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0025_auto_20180802_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_trainee',
            field=models.BooleanField(default=False, help_text='For a person who did made the capacitation offline', verbose_name='Is trainee'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]