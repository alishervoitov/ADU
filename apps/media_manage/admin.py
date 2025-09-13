from django.contrib import admin
from .models import NewType, News , DocumentType, Documents


class NewTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'description', 'created_at_str', 'updated_at_str')
    search_fields = ('name',)
    fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('name', 'slug', 'parent', 'description', 'created_at', 'updated_at', 'created_by', 'updated_by')
            }),
      )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'created_at_str', 'updated_at_str')
    search_fields = ('title',)
    list_filter = ('type',)

    fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('title', 'slug', 'type', 'image', 'viewed_count')
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


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at_str', 'updated_at_str')
    search_fields = ('name',)
    fieldsets = (
                  ('Asosiy ma\'lumotlar', {
                    'fields': ('name', 'slug', 'created_at', 'updated_at', 'created_by', 'updated_by')
                  }),
      )

    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'url', 'created_at_str', 'updated_at_str')
    search_fields = ('title',)
    list_filter = ('type',)

    fieldsets = (
            ('Asosiy ma\'lumotlar', {
                  'fields': ('title', 'type', 'slug', 'url', 'file')
            }),
            ('Tizim ma\'lumotlari', {
                  'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
                  'classes': ('collapse',)
            })
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'slug')


admin.site.register(NewType, NewTypeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Documents, DocumentsAdmin)