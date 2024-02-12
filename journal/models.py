from django.db import models
from django.utils import timezone


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




class Department(models.Model):
    class Meta:
        db_table = 'department'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    department = models.CharField(max_length=100, verbose_name="Название отдела")

    def __str__(self):
        return f"{self.department}"
    


class Journal(models.Model):
    class Meta:
        db_table = 'journal'
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел")
    username = models.CharField(max_length=255, verbose_name="Фамилия Имя Отчество")
    description = models.TextField(verbose_name="Описание проблемы")
    solution = models.TextField(verbose_name="Решение проблемы")
    tags = models.CharField(max_length=100, verbose_name="Теги")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.create_dt} {self.department} {self.username}"
    
