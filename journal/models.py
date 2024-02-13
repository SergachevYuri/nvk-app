from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _




# Create your models here.
'''
Технический журнал.
Сам журнал с данными.

Table - journal
date
department
name
description
solution
tags

'''

class Journal(models.Model):
    class Meta:
        db_table = 'journal'
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    department = models.ForeignKey("organization.Department", verbose_name=_("Отдел"), on_delete=models.CASCADE)
    username = models.CharField(max_length=255, verbose_name="Фамилия Имя Отчество")
    description = models.TextField(verbose_name="Описание проблемы")
    solution = models.TextField(verbose_name="Решение проблемы")
    tags = models.CharField(max_length=100, verbose_name="Теги")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.create_dt} {self.department} {self.username}"
    
