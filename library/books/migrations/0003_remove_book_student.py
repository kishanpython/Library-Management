# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-26 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='student',
        ),
    ]
