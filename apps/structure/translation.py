from modeltranslation.translator import TranslationOptions, register

from apps.structure.models import Divisions, MenuItem, Document, DivisionDocument


@register(Divisions)
class DivisionsTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(DivisionDocument)
class DivisionDocumentTranslationOptions(TranslationOptions):
    fields = ('name',)