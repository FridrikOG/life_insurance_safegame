# Generated by Django 4.0.5 on 2022-06-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_application_datecreated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='premium',
            new_name='age',
        ),
        migrations.AlterField(
            model_name='application',
            name='dateCreated',
            field=models.CharField(default=1655676622, max_length=255),
        ),
    ]