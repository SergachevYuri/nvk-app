from django.contrib import admin

from .models import Phonebook


class PhonebookAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'department', 'cabinet', 'bilding', 'sip', 'phone', 'email')
    search_fields = ('name', 'job_title', 'department', 'cabinet', 'bilding', 'sip', 'phone', 'email')
    list_filter = ('department', 'cabinet', 'bilding')


admin.site.register(Phonebook, PhonebookAdmin)