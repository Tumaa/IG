# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20191118_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Welcome Me!'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(default='Anonymous'),
        ),
    ]