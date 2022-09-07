from django.contrib import admin
from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('body',)
    
admin.site.register(Note, NoteAdmin)
