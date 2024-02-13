from django.contrib import admin

from .models import Phonebook


class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('department', 'cabinet', 'bilding', 'sip', 'phone', 'email')
    search_fields = ('department', 'cabinet', 'bilding', 'sip', 'phone', 'email')
    list_filter = ('department', 'cabinet', 'bilding', 'sip', 'phone', 'email')


admin.site.register(Phonebook, PhonebookAdmin)