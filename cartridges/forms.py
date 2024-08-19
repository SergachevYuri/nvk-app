from django import forms
from .models import Status

class CartridgeFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[('', 'Все')] + Status.choices,
        required=False,
        label='Статус'
    )
    order_by = forms.ChoiceField(
        choices=[
            ('date_added', 'Дата добавления'),
            ('status', 'Статус'),
            ('manufacturer', 'Производитель'),
            ('model', 'Модель')
        ],
        required=False,
        label='Сортировать по'
    )
