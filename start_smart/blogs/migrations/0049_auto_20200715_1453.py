# Generated by Django 3.0.2 on 2020-07-15 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0048_auto_20200713_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 15, 14, 53, 58, 561727)),
        ),
    ]