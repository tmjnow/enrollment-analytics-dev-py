# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='semester_code',
            field=models.PositiveIntegerField(),
        ),
    ]
