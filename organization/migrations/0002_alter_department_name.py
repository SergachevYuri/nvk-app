# Generated by Django 5.0.2 on 2024-08-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отдел'),
        ),
    ]
