# Generated by Django 4.0.5 on 2022-07-12 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='dateExpires',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 0, 0), max_length=255),
        ),
    ]
