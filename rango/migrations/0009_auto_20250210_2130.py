# Generated by Django 2.2.28 on 2025-02-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20250210_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
