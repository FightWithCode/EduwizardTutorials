# Generated by Django 2.2 on 2020-06-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200617_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='front_image_233',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='front_image_500',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
