# Generated by Django 2.2.28 on 2025-02-10 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20250210_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
