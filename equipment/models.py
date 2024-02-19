from tabnanny import verbose
from django.db import models

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
    serial_number = models.CharField(verbose_name="Серийный номер", max_length=100, blank=True)
    inventory_number = models.CharField(verbose_name="Инвентарынй номер", max_length=100, blank=True)
    manufacturer = models.CharField(verbose_name="Производитель", max_length=100)
    model = models.CharField(verbose_name="Модель", max_length=100) 
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW, verbose_name="Статус")
    department = models.ForeignKey('organization.Department', verbose_name="Отдел / Подразделение", on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    notes = models.TextField(verbose_name="Записи", blank=True)




class TypeEquipment(models.Model):

    class Meta:
        db_table = "type_equipment"
        verbose_name = "Тип Оборудования"
        verbose_name_plural = "Типы Оборудования"


    name = models.CharField(max_length=100)