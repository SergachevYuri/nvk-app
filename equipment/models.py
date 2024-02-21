from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class Status(models.TextChoices):
    '''
    Статусы оборудования
    '''
    NEW = 'NEW', _('Новый')
    IN_WORK = 'IN_WORK', _("В Работе")
    IN_REPAIR = 'IN_REPAIR', _("В Ремонте")
    BROKEN = 'BROKEN', _("Сломан")
    ON_WRITE_OFF = 'ON_WRITE_OFF', _("На списание")
    WRITE_OFF = 'WRITE_OFF', _("Списанно")



'''
Оборудование
'''
class Equipment(models.Model):

    class Meta:
        db_table = "equipment"
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


    name = models.CharField(verbose_name="Название", max_length=100)
    type = models.ForeignKey('TypeEquipment', verbose_name="Тип", on_delete=models.SET_NULL, blank=True, null=True)
    serial_number = models.CharField(verbose_name="Серийный номер", unique=True, max_length=100, blank=True)
    inventory_number = models.CharField(verbose_name="Инвентарынй номер", unique=True, max_length=100, blank=True)
    manufacturer = models.ForeignKey('EquipmentManufacture', verbose_name="Производитель", on_delete=models.SET_NULL, blank=True, null=True)
    model = models.CharField(verbose_name="Модель", max_length=100) 
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW, verbose_name="Статус")
    department = models.ForeignKey('organization.Department', verbose_name="Отдел / Подразделение", on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    notes = models.TextField(verbose_name="Записи", blank=True)
    is_component = models.BooleanField(default=False, verbose_name="Является составным")
    parent_equipment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='components', verbose_name="Основное оборудование")



    def __str__(self):
        return f"{self.name} - {self.model}"




class TypeEquipment(models.Model):

    class Meta:
        db_table = "type_equipment"
        verbose_name = "Тип Оборудования"
        verbose_name_plural = "Типы Оборудования"


    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class EquipmentStatusHistory(models.Model):

    class Meta:
        db_table = "equipment_status_history"
        verbose_name = "История статусов оборудования"
        verbose_name_plural = "Истории статусов оборудования"


    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Оборудование")
    previous_status = models.CharField(max_length=20, choices=Status.choices, verbose_name="Предыдущий статус")
    new_status = models.CharField(max_length=20, choices=Status.choices, verbose_name="Новый статус")
    change_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения")
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Изменено пользователем")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")


    def __str__(self):
        return f"{self.equipment.name} - {self.new_status} on {self.change_date}"



class EquipmentManufacture(models.Model):

    class Meta:
        db_table = "equipment_manufacture"
        verbose_name = "Производитель оборудования"
        verbose_name_plural = "Производители оборудования"


    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name