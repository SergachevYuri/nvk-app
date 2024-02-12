from django.contrib import admin

from .models import Journal, Department

# Register your models here.

class JournalAdmin(admin.ModelAdmin):
    list_display = ('department', 'username', 'description', 'create_dt', 'tags')
    search_fields = ('department', 'username', 'description', 'create_dt', 'tags')
    list_filter = ('department', 'username', 'description', 'create_dt', 'tags')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', )




admin.site.register(Journal, JournalAdmin)
admin.site.register(Department, DepartmentAdmin)