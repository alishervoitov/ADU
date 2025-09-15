from django.contrib import admin
from .models import (
     InteractiveService,
     FAQ,
     Contact
)

@admin.register(InteractiveService)
class InteractiveServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('order', 'created_at')
    
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
     list_display = ('question', 'answer', 'is_active', 'order',  'updated_at')
     search_fields = ('question',)
     list_filter = ('is_active',)
     ordering = ('order', 'created_at')
     
     readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'message', 'created_at', 'updated_at')
    search_fields = ('full_name', 'phone', 'message')
    ordering = ('-created_at',)
    
    readonly_fields = ('full_name', 'phone', 'message', 'created_at', 'updated_at', 'created_by', 'updated_by')
