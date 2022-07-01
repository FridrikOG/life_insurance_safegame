# Generated by Django 4.0.5 on 2022-06-30 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0010_alter_insurance_dateapproved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='dateExpires',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 30, 0, 0), max_length=255),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='premium',
            field=models.IntegerField(),
        ),
    ]