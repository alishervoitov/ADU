from modeltranslation.translator import TranslationOptions, register

from apps.blog.models import InteractiveService

@register(InteractiveService)
class InteractiveServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")
