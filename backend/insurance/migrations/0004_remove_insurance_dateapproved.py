# Generated by Django 4.0.5 on 2022-06-24 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_insurance_dateapproved_insurance_datecreated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='dateApproved',
        ),
    ]
