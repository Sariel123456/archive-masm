# Generated by Django 4.2.20 on 2025-05-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='titre',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='titre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
