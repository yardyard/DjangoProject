# Generated by Django 3.2.12 on 2022-02-19 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_thangks'),
    ]

    operations = [
        migrations.AddField(
            model_name='thangks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
