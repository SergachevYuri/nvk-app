from django.contrib import admin

from .models import Journal, Tag

# Register your models here.

class JournalAdmin(admin.ModelAdmin):
    list_display = ('department', 'username', 'description', 'create_dt', 'get_tags')
    search_fields = ('department', 'username', 'description', 'create_dt', 'tags')
    list_filter = ('department', 'username', 'description', 'create_dt', 'tags')

    def get_tags(self, obj):
        return ", ".join([p.name for p in obj.tags.all()])




class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.register(Tag, TagAdmin)
admin.site.register(Journal, JournalAdmin)
