# Generated by Django 4.0.5 on 2022-06-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_application_approved_alter_application_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='dateCreated',
            field=models.CharField(default=1655729989, max_length=255),
        ),
    ]
