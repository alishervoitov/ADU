from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . import models


@admin.register(models.VersionHistory)
class VersionHistoryAdmin(TranslationAdmin):
    list_display = ("id", "version", "required", "created_at", "updated_at")
    list_display_links = ("id", "version")
    list_filter = ("required", "created_at", "updated_at")
    search_fields = ("version",)


@admin.register(models.FrontendTranslation)
class FrontTranslationAdmin(TranslationAdmin):
    list_display = ("id", "key", "text", "created_at", "updated_at")
    list_display_links = ("id", "key")
    list_filter = ("created_at", "updated_at")
    search_fields = ("key", "text")
    
    # TranslationAdmin avtomatik ravishda barcha til maydonlarini ko'rsatadi
    # Qo'shimcha fieldsets kerak emas
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
