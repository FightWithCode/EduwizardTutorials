# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-08 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='chapter',
            field=models.CharField(default='h', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='note_class',
            field=models.CharField(default='h', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.CharField(default='a', max_length=25),
            preserve_default=False,
        ),
    ]
