# Generated by Django 3.0.8 on 2020-07-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_auto_20200713_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='finances',
            name='transactions',
            field=models.TextField(default=''),
        ),
    ]
