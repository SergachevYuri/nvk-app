# Generated by Django 5.0.2 on 2024-02-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartridges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='inventory_number',
            field=models.CharField(max_length=100, unique=True, verbose_name='Инвертизационный номер'),
        ),
    ]
