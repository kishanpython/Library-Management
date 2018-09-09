# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-10 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20180809_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobno', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='student_prof',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student_prof',
        ),
    ]
