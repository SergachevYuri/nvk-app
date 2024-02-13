from django.db import models
from django.utils.translation import gettext_lazy as _



class Phonebook(models.Model):


    class BUILDING(models.TextChoices):
        RK = 'RK', _('Редакторский Корпус')
        TD = 'TD', _('Теледом')
        PV = 'PV', _('Павилион')
        PTVS = 'PTVS', _('ПТВС')
        GAR = 'GAR', _('Гараж')

    class Meta:
        db_table = 'phonebook'
        verbose_name = 'Телефонная книга'
        verbose_name_plural = 'Телефонная книга'



    name = models.CharField(max_length=255, verbose_name="ФИО", unique=True, blank=True, null=True)
    cabinet = models.CharField(max_length=255, verbose_name="Кабинет")
    bilding = models.CharField(max_length=4, choices=BUILDING.choices, default=BUILDING.RK, verbose_name="Корпус")
    department = models.ForeignKey('organization.Department', on_delete=models.CASCADE, verbose_name="Отдел")
    sip = models.CharField(max_length=255, verbose_name="SIP телефон", blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name="Городский телефон", blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name="Почта", blank=True, null=True)
    

    def __str__(self):
        return self.sip

