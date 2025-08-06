import factory
from factory.django import DjangoModelFactory
from factory.declarations import Sequence, LazyFunction, LazyAttribute
from faker import Faker
import random

from .models import FrontendTranslation
from apps.users.models import User

fake = Faker('uz_UZ')  # Uzbek locale


class FrontendTranslationFactory(DjangoModelFactory):
    """FrontendTranslation model uchun Factory"""
    
    class Meta:
        model = FrontendTranslation
        django_get_or_create = ('key',)
    
    key = Sequence(lambda n: f"translation_key_{n:04d}")
    text = LazyFunction(lambda: fake.sentence(nb_words=6))
    
    # Model translation maydonlari uchun
    text_uz = LazyAttribute(lambda obj: obj.text)
    text_uz_cyrl = LazyFunction(lambda: fake.sentence(nb_words=6))
    text_ru = LazyFunction(lambda: fake.sentence(nb_words=6))
    text_en = LazyFunction(lambda: fake.sentence(nb_words=6))
