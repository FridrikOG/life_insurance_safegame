# Generated by Django 4.0.6 on 2022-07-27 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField(default=0)),
                ('isPaid', models.BooleanField(default=False)),
                ('datePaid', models.DateTimeField(auto_now_add=True)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.insurance')),
            ],
        ),
    ]
