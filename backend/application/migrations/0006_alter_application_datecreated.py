# Generated by Django 4.0.5 on 2022-06-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_application_active_alter_application_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='dateCreated',
            field=models.CharField(default=1655731716, max_length=255),
        ),
    ]
