from django.contrib import admin
from .models import NewType, News , DocumentType, Documents


class NewTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent', 'description', 'created_at_str', 'updated_at_str')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    list_filter = ('parent',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'video_url', 'type', 'created_at_str', 'updated_at_str')
    search_fields = ('title',)
    list_display_links = ('id', 'title')
    list_filter = ('type',)

    readonly_fields = ('viewed_count', 'updated_at', 'created_by', 'updated_by')
    
    def save_model(self, request, obj, form, change):
        if change:
            update_fields = []

            for field in form.changed_data:
                update_fields.append(field)

            if update_fields:
                obj.save(update_fields=update_fields)
            else:
                obj.save()
        else:
            obj.save()


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at_str', 'updated_at_str')
    search_fields = ('name',)
    list_display_links = ('id', 'name')

    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'type', 'url', 'created_at_str', 'updated_at_str')
    search_fields = ('title',)
    list_display_links = ('id', 'title')
    list_filter = ('type',)

    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'slug')


admin.site.register(NewType, NewTypeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Documents, DocumentsAdmin)