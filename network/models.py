from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

   
class IPAM(models.Model):
    class Meta:
        db_table = "ipam"
        verbose_name = "IP"
        verbose_name_plural = "1. IP"

    ip_address = models.GenericIPAddressField(unique=True, default='127.0.0.1')
    subnet_mask = models.CharField(max_length=15, default='255.255.255.0')  # Example: 255.255.255.0
    gateway = models.GenericIPAddressField(blank=True, null=True)
    dns_servers = models.CharField(max_length=255, blank=True)  # Comma-separated list of DNS servers
    hostname = models.CharField(max_length=100, blank=True)
    port = models.ForeignKey('Ports', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    assigned_to = models.CharField(max_length=100, blank=True)  # Who the IP is assigned to
    date_assigned = models.DateTimeField(auto_now_add=True)  # Use auto_now_add

    def __str__(self):
        return str(self.ip_address)



class Switch(models.Model):
    class Meta:
        db_table = "switch"
        verbose_name = "Свитч"
        verbose_name_plural = "2. Свитч"


    hostname = models.CharField(max_length=100, verbose_name="Хостнейм")
    manufacturer = models.CharField(max_length=100, blank=True, verbose_name="Производитель")
    model = models.CharField(max_length=100, blank=True, verbose_name="Модель")
    serial_number = models.CharField(max_length=50, blank=True, verbose_name="Серийный номер")
    location = models.CharField(max_length=255, blank=True, verbose_name="Местоположение")

    def __str__(self):
        return self.hostname




class Ports(models.Model):
    class Meta:
        db_table = "ports"
        verbose_name = "Порты"
        verbose_name_plural = "3. Порты"


    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)
    number = models.CharField(default='0')
    description = models.CharField(max_length=255, blank=True)
    vlan = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4094)],
        blank=True, null=True
    )  # VLAN ID, optional

    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive')

    def __str__(self):
        return f"{self.switch.hostname} - Port {self.number}"
    