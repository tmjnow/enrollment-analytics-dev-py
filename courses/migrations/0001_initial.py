# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_code', models.PositiveIntegerField(unique=True)),
                ('semester_title', models.CharField(max_length=255)),
                ('crn_number', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('section_number', models.PositiveIntegerField()),
                ('max_enrollment', models.PositiveIntegerField()),
                ('act_enrollment', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField(default='Description not provided.')),
                ('catalog_version', models.CharField(default='Version not provided.', max_length=512)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('department', 'number', 'title')]),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
