from django.db import models
# Create your models here.


class News(models.Model):
    class Meta:
        db_table = "news"
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


    title_name = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    describtion = models.CharField(max_length=255, verbose_name="Описание")
    content = models.TextField(default='', verbose_name="Содержание")
    category = models.ManyToManyField(max_length=50, verbose_name="Категория")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    username = models.CharField(max_length=20, verbose_name="Пользователь")
    