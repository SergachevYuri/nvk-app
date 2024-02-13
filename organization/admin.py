from django.contrib import admin

from .models import Directorate, Department


class DirectorateAdmin(admin.ModelAdmin):
    list_display = ('name', )




class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'directorate')
    search_fields = ('name', 'directorate')
    list_filter = ['directorate']




admin.site.register(Directorate, DirectorateAdmin)
admin.site.register(Department, DepartmentAdmin)