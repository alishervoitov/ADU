from modeltranslation.translator import TranslationOptions, register

from apps.media_manage.models import News, NewType, DocumentType, Documents

@register(NewType)
class NewTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(DocumentType)
class DocumentTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Documents)
class DocumentsTranslationOptions(TranslationOptions):
    fields = ('title',)