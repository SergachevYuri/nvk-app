# Generated by Django 5.0.2 on 2024-08-01 06:49

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipam',
            options={'verbose_name': 'IP', 'verbose_name_plural': '1. IP'},
        ),
        migrations.RemoveField(
            model_name='ports',
            name='active',
        ),
        migrations.RemoveField(
            model_name='ports',
            name='port',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='switch',
            name='manafacture',
        ),
        migrations.AddField(
            model_name='ipam',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ipam',
            name='date_assigned',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ipam',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='ipam',
            name='dns_servers',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='ipam',
            name='gateway',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ipam',
            name='hostname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ipam',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', unique=True),
        ),
        migrations.AddField(
            model_name='ipam',
            name='port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network.ports'),
        ),
        migrations.AddField(
            model_name='ipam',
            name='subnet_mask',
            field=models.CharField(default='255.255.255.0', max_length=15),
        ),
        migrations.AddField(
            model_name='ports',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='ports',
            name='number',
            field=models.CharField(default='0'),
        ),
        migrations.AddField(
            model_name='ports',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=20),
        ),
        migrations.AddField(
            model_name='ports',
            name='vlan',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4094)]),
        ),
        migrations.AddField(
            model_name='switch',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='Местоположение'),
        ),
        migrations.AddField(
            model_name='switch',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='switch',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Серийный номер'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='hostname',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='switch',
            name='model',
            field=models.CharField(blank=True, max_length=100, verbose_name='Модель'),
        ),
    ]