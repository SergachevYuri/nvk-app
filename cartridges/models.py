from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Status(models.TextChoices):
    REFILLED = 'RFD', _('Заправленный')
    WAITING_FOR_REFILL = 'WAIT', _('Ожидание заправки')
    REFILLING = 'RF', _('На заправке')
    CHECKING = 'CH', _('На проверке')
    ON_THE_JOB = 'OTJ', _('В работе')

class Cartridge(models.Model):
    class Meta:
        db_table = "cartridges"
        verbose_name = "Картриджи"
        verbose_name_plural = "1. Картриджи"


    inventory_number = models.CharField(max_length=100, unique=True, verbose_name="Инвертизационный номер")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    model = models.CharField(max_length=100, verbose_name="Модель")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AWAITING_REFILL, verbose_name="Статус")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    status_updated = models.DateTimeField(auto_now=True, verbose_name="Время обновления статуса")

    def __str__(self):
        return f"{self.inventory_number} - {self.manufacturer} {self.model}"
    
    def update_status(self, new_status, page_count=None):
        # Логика обновления статуса...
        if new_status == Status.AWAITING_REFILL:
            if page_count is not None:
                # Пытаемся найти последнюю запись PrintRecord без end_page_count
                last_record = self.printrecord_set.filter(end_page_count__isnull=True, cartridge_id=self.id).last()
                if last_record:
                    # Если запись найдена, обновляем её
                    last_record.end_page_count = page_count
                    last_record.save()
                else:
                    # Если подходящая запись не найдена, создаём новую
                    PrintRecord.objects.create(cartridge=self, start_page_count=page_count)
        elif new_status == Status.IN_USE:
            if page_count is not None:
                # Создание новой записи при установке картриджа в принтер
                PrintRecord.objects.create(cartridge=self, start_page_count=page_count, end_page_count=None)
        self.status = new_status
        self.save()


class RefillRecord(models.Model):
    class Meta:
        db_table = "refill_record"
        verbose_name = "Заправка"
        verbose_name_plural = "2. Заправка"

    refill_number = models.CharField(max_length=100, unique=True, verbose_name="Номер заправки")
    cartridges = models.ManyToManyField(Cartridge, verbose_name="Картриджи")
    date_sent = models.DateTimeField(default=timezone.now, verbose_name="Дата отправки на заправку")
    notice = models.TextField(default='', verbose_name="Примечание")
    date_returned = models.DateTimeField(null=True, blank=True, verbose_name="Дата возврата")

    def __str__(self):
        return f"Заправка №{self.refill_number} от {self.date_sent.strftime('%Y-%m-%d')}"



class PrintRecord(models.Model):
    class Meta:
        db_table = "print_record"
        verbose_name = "Отпечатки"
        verbose_name_plural = "3. Отпечатки"


    cartridge = models.ForeignKey(Cartridge, on_delete=models.CASCADE, verbose_name="Картридж")
    start_page_count = models.IntegerField(verbose_name="Количество страниц при установке")
    end_page_count = models.IntegerField(verbose_name="Количество страниц перед заправкой", null=True, blank=True)
    date_recorded = models.DateTimeField(default=timezone.now, verbose_name="Дата установки")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.cartridge} - Страниц отпечатано: {self.end_page_count - self.start_page_count if self.end_page_count else 'Идет печать'}"
    
    @property
    def pages_printed(self):
        """Вычисляет разницу между начальным и конечным количеством страниц."""
        if self.end_page_count is not None:
            return self.end_page_count - self.start_page_count
        return None
