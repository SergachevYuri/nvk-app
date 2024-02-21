# Generated by Django 5.0.2 on 2024-02-20 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentManufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Производитель оборудования',
                'verbose_name_plural': 'Производители оборудования',
                'db_table': 'equipment_manufacture',
            },
        ),
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.equipmentmanufacture', verbose_name='Производитель'),
        ),
    ]
