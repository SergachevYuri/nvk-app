from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.

class NewsCategory(models.Model):
    class Meta:
        db_table = "news_category"
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категория новостей"

    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        db_table = "news"
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


    title_name = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    describtion = models.CharField(max_length=255, verbose_name="Описание")
    content = models.TextField(default='', verbose_name="Содержание")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", default=None, editable=False)

    def __str__(self):
        return self.title_name

    def save(self, *args, **kwargs):
        # Check if the object is being created (not updated)
        if not self.pk:
            # Set the author to the currently logged-in user
            self.author = User.objects.get(pk=settings.AUTH_USER_MODEL)
        super(News, self).save(*args, **kwargs)
