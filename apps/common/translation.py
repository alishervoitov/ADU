from modeltranslation.translator import TranslationOptions, register

from apps.common import models


@register(models.FrontendTranslation)
class FrontTranslationOptions(TranslationOptions):
    fields = ("text",)
