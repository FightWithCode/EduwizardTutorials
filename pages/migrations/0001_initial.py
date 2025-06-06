# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-05 16:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('mobile_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Please Enter Correct Mobile Number...', regex='^\\d{10}$')])),
                ('subject_or_class', models.CharField(choices=[('Class VI', 'Class VI'), ('Class VII', 'Class VII'), ('Class VIII', 'Class VIII'), ('Class IX', 'Class IX'), ('Class X', 'Class X'), ('Class XI', 'Class XI'), ('Class XII', 'Class XII'), ('Others', 'Others')], max_length=50)),
            ],
        ),
    ]
