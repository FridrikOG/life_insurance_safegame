# Generated by Django 4.0.5 on 2022-07-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0012_alter_insurance_dateexpires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='dateExpires',
            field=models.DateTimeField(default=None, max_length=255),
        ),
    ]
