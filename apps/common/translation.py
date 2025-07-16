# translation.py
from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.FrontendTranslation)
class FrontTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(models.VersionHistory)
class VersionHistoryTranslationOptions(TranslationOptions):
    fields = ("version",)
