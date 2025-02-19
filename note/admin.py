from django.contrib import admin
from .models import Notes, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('note_title', 'created_at', 'category')
    search_fields = ('note_title', 'note')
    list_filter = ('category',)