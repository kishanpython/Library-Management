# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-09 08:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180909_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocate',
            name='upto',
        ),
        migrations.AlterField(
            model_name='allocate',
            name='allodate',
            field=models.DateField(default=datetime.date(2018, 9, 9)),
        ),
    ]
