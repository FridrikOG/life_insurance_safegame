# Generated by Django 4.0.5 on 2022-07-12 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
