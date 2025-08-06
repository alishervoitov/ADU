import factory
from factory.django import DjangoModelFactory
from factory.declarations import Sequence, LazyFunction, LazyAttribute
from faker import Faker
import random

from .models.services import InteractiveService
from apps.users.models import User

fake = Faker('uz_UZ')  # Uzbek locale


class InteractiveServiceFactory(DjangoModelFactory):
    """InteractiveService model uchun Factory"""
    
    class Meta:
        model = InteractiveService
        django_get_or_create = ('name',)
    
    name = LazyFunction(lambda: random.choice([
        "Onlayn kutubxona", "Elektron darslar", "Student portali", "Professor portali",
        "Imtihon tizimi", "Reyting tizimi", "Stipendiya tizimi", "Talabalar uyushmasi",
        "Ilmiy tadqiqotlar", "Konferensiya tizimi", "Jurnallar bazasi", "Tez yordam",
        "IT yordam", "Akademik maslahat", "Psixologik yordam", "Huquqiy maslahat",
        "Karyera markazi", "Biznes inkubator", "Innovatsiya markazi", "Til markazi"
    ]))
    
    description = LazyFunction(lambda: fake.text(max_nb_chars=300))
    link = LazyFunction(lambda: fake.url())
    is_active = LazyFunction(lambda: random.choice([True, True, True, False]))  # 75% faol
    order = Sequence(lambda n: n * 10)
    
    # Icon va icon_dark maydonlari null bo'ladi chunki ular FileField
