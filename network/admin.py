from django import forms
from django.db import models
from django.contrib import admin
from .models import IPAM, Switch, Ports

# Register your models here.

@admin.register(IPAM)
class IpamAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'subnet_mask', 'gateway', 'hostname', 'port', 'description', 'assigned_to', 'date_assigned', 'get_vlan')  # Add 'get_vlan' to list_display
    search_fields = ('ip_address', 'hostname', 'description', 'assigned_to')
    list_filter = ('port__vlan', 'port', 'date_assigned')
    ordering = ('port__vlan',)  # Add ordering by VLAN

    def get_vlan(self, obj):
        return obj.port.vlan if obj.port else None
    get_vlan.short_description = 'VLAN'

@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'manufacturer', 'model', 'serial_number', 'location')
    search_fields = ('hostname', 'manufacturer', 'model', 'serial_number', 'location')

@admin.register(Ports)
class PortsAdmin(admin.ModelAdmin):
    list_display = ('switch', 'number', 'description', 'vlan', 'status')
    list_filter = ('switch', 'vlan', 'status')
    search_fields = ('switch__hostname', 'description')
