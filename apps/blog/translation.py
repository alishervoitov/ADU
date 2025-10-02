from modeltranslation.translator import TranslationOptions, register

from apps.blog.models import InteractiveService, FAQ

@register(InteractiveService)
class InteractiveServiceTranslationOptions(TranslationOptions):
    fields = ("name", )


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")
