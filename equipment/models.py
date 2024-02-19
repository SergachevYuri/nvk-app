from django.db import models

class Equipment(models.Model):

    class Meta:
        db_table = "equipment"
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


    name = models.CharField(max_length=100)
    type = models.ForeignKey('TypeEquipment', on_delete=models.SET_NULL, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True)
    inventory_number = models.CharField(max_length=100, blank=True)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_of_manufacture = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)




class TypeEquipment(models.Model):

    class Meta:
        db_table = "type_equipment"
        verbose_name = "Тип Оборудования"
        verbose_name_plural = "Типы Оборудования"


    name = models.CharField(max_length=100)