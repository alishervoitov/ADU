import factory
from factory.django import DjangoModelFactory
from factory.declarations import LazyFunction, SubFactory, LazyAttribute
from faker import Faker
import random
from datetime import date, timedelta

from ..models.main_info import HomePageText, MENU_PARTS

fake = Faker('uz_UZ')  # Uzbek locale

class HomePageTextFactory(DjangoModelFactory):
    type = LazyFunction(lambda: random.choice(MENU_PARTS)[0])
    title = LazyFunction(lambda: fake.sentence(nb_words=6))
    description = LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    url = LazyAttribute(lambda obj: f"https://adu.uz/{obj.type}" if obj.type == 'main' else None)
    created_at = LazyFunction(lambda: date.today() - timedelta(days=random.randint(0, 365)))
    updated_at = LazyFunction(lambda: date.today())

    class Meta:
        model = HomePageText
