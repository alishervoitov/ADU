from django.contrib import admin
from .models import (
     InteractiveService
)

@admin.register(InteractiveService)
class InteractiveServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('order', 'created_at')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'icon', 'icon_dark', 'description', 'link', 'is_active', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
     