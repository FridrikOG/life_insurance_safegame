# Generated by Django 4.0.5 on 2022-06-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_alter_application_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='dateCreated',
            field=models.CharField(default=1655736425, max_length=255),
        ),
    ]