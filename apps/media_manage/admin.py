from django.contrib import admin
from .models import NewType, News


class NewTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at_str', 'updated_at_str')
    search_fields = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at_str', 'updated_at_str')
    search_fields = ('title',)
    list_filter = ('type',)

    fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('title', 'type', 'viewed_count')
            }),
            ('Kontent', {
                  'fields': ('content',)
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
    )
    readonly_fields = ('viewed_count', 'created_at', 'updated_at', 'created_by', 'updated_by')

admin.site.register(NewType, NewTypeAdmin)
admin.site.register(News, NewsAdmin)