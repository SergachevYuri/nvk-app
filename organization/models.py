from django.db import models
from django.utils.translation import gettext_lazy as _


class Directorate(models.Model):

    class Meta:
        db_table = "directorate"
        verbose_name = "Дирекция"
        verbose_name_plural = "Дирекция"

    name = models.CharField(_("Название дирекции"), max_length=255)


    def __str__(self):
        return self.name
    

class Department(models.Model):

    class Meta:
        db_table = "department"
        verbose_name = "Отдел"
        verbose_name_plural = "Отдел"

    
    directorate = models.ForeignKey("Directorate", verbose_name=_("Дирекция"), on_delete=models.CASCADE)
    name = models.CharField(_("Отдел"), max_length=255)


    def __str__(self):
        return f"{self.directorate} - {self.name}"
    
    def get_name(self):
        return self.name
    
    def get_directorate(self):
        return self.directorate