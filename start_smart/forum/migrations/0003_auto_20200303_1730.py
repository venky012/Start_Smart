# Generated by Django 3.0.1 on 2020-03-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200303_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
