from django.contrib import admin
from .models import Equipment, TypeEquipment, EquipmentManufacture

# Register your models here.


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'manufacturer', 'model', 'status', 'department', 'parent_equipment', 'is_component')
    list_filter = ('status', 'manufacturer', 'type', 'is_component')
    search_fields = ('manufacturer', 'model', 'type')


@admin.register(TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(EquipmentManufacture)
class EquipmentManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

