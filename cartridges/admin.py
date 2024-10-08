from django import forms
from django.db import models
from django.contrib import admin
from django.utils import timezone
from .models import Cartridge, RefillRecord, PrintRecord, Status


class CartridgeAdminForm(forms.ModelForm):
    page_count = forms.IntegerField(required=True, label='Количество страниц', help_text='Введите текущее количество страниц при смене статуса.')

    class Meta:
        model = Cartridge
        fields = '__all__'


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            refill_count=models.Count('refillrecord', distinct=True)
        )

    def refill_count(self, obj):
        """Returns the refill count for the cartridge."""
        return obj.refill_count

    refill_count.short_description = "Количество заправок"  # Переименование заголовка колонки

    list_display = ('inventory_number', 'manufacturer', 'model', 'status', 'date_added', 'status_updated', 'refill_count')
    list_filter = ('status', 'manufacturer', 'date_added')
    search_fields = ('inventory_number', 'manufacturer', 'model')

    form = CartridgeAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(CartridgeAdmin, self).get_form(request, obj, **kwargs)
        if obj and obj.status in [Status.REFILLED, Status.ON_THE_JOB]:  # Проверяем статус объекта
            form.base_fields['page_count'].required = True  # Делаем поле ОБЯЗАТЕЛЬНЫМ  
        else:
            form.base_fields.pop('page_count', None)  # Удаляем поле из формы, если статус не подходит
        return form

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        page_count = form.cleaned_data.get('page_count', None)
        if page_count is not None:
            # Проверка и обновление PrintRecord, как описано ранее
            obj.update_status(obj.status, page_count)



class RefillRecordForm(forms.ModelForm):
    class Meta:
        model = RefillRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RefillRecordForm, self).__init__(*args, **kwargs)
        # Получаем уже выбранные картриджи, если они есть
        if self.instance.pk:
            self.fields['cartridges'].queryset = Cartridge.objects.filter(
                models.Q(status=Status.WAITING_FOR_REFILL) | 
                models.Q(refillrecord=self.instance)  # Добавляем картриджи, уже выбранные для этой заправки
            )
        else:
            self.fields['cartridges'].queryset = Cartridge.objects.filter(status=Status.WAITING_FOR_REFILL)

        # Добавляем поле для даты возврата с заправки
        self.fields['date_returned'] = forms.DateTimeField(
            label='Дата возврата с заправки',
            required=False,  # Поле не обязательно для заполнения
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        )


@admin.register(RefillRecord)
class RefillRecordAdmin(admin.ModelAdmin):
    readonly_fields=('date_returned', )

    form = RefillRecordForm
    list_display = ('refill_number', 'date_sent', 'date_returned')
    list_filter = ('date_sent', 'date_returned')
    search_fields = ('refill_number',)
    filter_horizontal = ('cartridges',)

    actions = ['mark_as_checked']  # Добавляем действие "Пометить как проверенные"

    def mark_as_checked(self, request, queryset):
        """Помечает выбранные картриджи как "На проверке" и устанавливает время возврата."""
        updated_count = 0
        for refill_record in queryset:
            for cartridge in refill_record.cartridges.all():
                if cartridge.status == Status.REFILLING:
                    cartridge.status = Status.CHECKING
                    cartridge.status_updated = timezone.now()  # Устанавливаем время возврата
                    cartridge.save()
                    updated_count += 1
            refill_record.date_returned = timezone.now()  # Устанавливаем время возврата
            refill_record.save()
        self.message_user(request, f"Обновлено {updated_count} картриджей.")

    mark_as_checked.short_description = "Поместить на проверку"

    def save_related(self, request, form, formsets, change):
        super(RefillRecordAdmin, self).save_related(request, form, formsets, change)
        cartridges = form.instance.cartridges.all()
        for cartridge in cartridges:
            cartridge.status = Status.REFILLING  # Обновляем статус на "На заправке"
            cartridge.save()


@admin.register(PrintRecord)
class PrintRecordAdmin(admin.ModelAdmin):
    list_display = ('cartridge', 'start_page_count', 'end_page_count', 'display_pages_printed', 'date_recorded')
    list_filter = ('date_recorded', 'cartridge')
    readonly_fields = ('display_pages_printed',)

    def display_pages_printed(self, obj):
        """Возвращает вычисленное количество отпечатанных страниц для отображения."""
        return obj.pages_printed if obj.pages_printed is not None else 'Идет печать'
    display_pages_printed.short_description = "Отпечатано страниц"




#admin.site.register(Cartridge, CartridgeAdmin)
#admin.site.register(RefillRecord, RefillRecordAdmin)
#admin.site.register(PrintRecord, PrintRecordAdmin)

