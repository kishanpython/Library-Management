# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-26 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_allocate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocate',
            name='aid',
            field=models.CharField(max_length=4),
        ),
    ]
