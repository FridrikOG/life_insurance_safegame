# Generated by Django 4.0.5 on 2022-06-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0006_alter_insurance_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='dateCreated',
            field=models.CharField(default=1655731744, max_length=255),
        ),
    ]
