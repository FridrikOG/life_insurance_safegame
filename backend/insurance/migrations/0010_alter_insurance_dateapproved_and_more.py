# Generated by Django 4.0.5 on 2022-06-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0009_insurance_datemodified_alter_insurance_dateapproved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='dateApproved',
            field=models.DateTimeField(auto_now=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='dateExpires',
            field=models.DateTimeField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='dateModified',
            field=models.DateTimeField(auto_now_add=True, max_length=255),
        ),
    ]
