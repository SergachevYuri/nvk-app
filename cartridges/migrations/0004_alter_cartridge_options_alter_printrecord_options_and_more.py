# Generated by Django 5.0.2 on 2024-02-13 07:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "cartridges",
            "0003_alter_cartridge_options_alter_printrecord_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cartridge",
            options={
                "verbose_name": "Картриджи",
                "verbose_name_plural": "1. Картриджи",
            },
        ),
        migrations.AlterModelOptions(
            name="printrecord",
            options={
                "verbose_name": "Отпечатки",
                "verbose_name_plural": "3. Отпечатки",
            },
        ),
        migrations.AlterModelOptions(
            name="refillrecord",
            options={"verbose_name": "Заправка", "verbose_name_plural": "2. Заправка"},
        ),
    ]
