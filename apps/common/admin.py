from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.common import models


# @admin.register(models.FrontendTranslation)
# class FrontTranslationAdmin(TranslationAdmin):
#     list_display = ("id", "key", "text", "created_at", "updated_at")
#     list_display_links = ("id", "key")
#     list_filter = ("created_at", "updated_at")
#     search_fields = ("key", "text")
#     readonly_fields = ("created_at", "updated_at", "created_by", "updated_by")

#     # class Media:
#     #     js = (
#     #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#     #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#     #         'modeltranslation/js/tabbed_translation_fields.js',
#     #     )
#     #     css = {
#     #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#     #     }
