import factory
from factory.django import DjangoModelFactory
from factory.declarations import Sequence, LazyFunction, LazyAttribute
from faker import Faker
import random

from .models.services import InteractiveService
from .models.faq import FAQ
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


class FAQFactory(DjangoModelFactory):
    """FAQ model uchun Factory"""
    
    class Meta:
        model = FAQ
        django_get_or_create = ('question',)
    
    question = LazyFunction(lambda: random.choice([
        "Universitetga qanday qilib kirish mumkin?",
        "Kontrakt to'lovi qancha?",
        "Grant imkoniyatlari mavjudmi?",
        "Yotoqxona xizmati bormi?",
        "Chet tillarni o'rganish imkoniyatlari qanday?",
        "Ilmiy tadqiqot ishlari qanday amalga oshiriladi?",
        "Bitiruvchilar uchun ish o'rinlari taklif qilinadimi?",
        "Onlayn ta'lim imkoniyatlari mavjudmi?",
        "Stipendiya olish shartlari qanday?",
        "Kutubxona xizmatlari qanday?",
        "Sport va madaniy faoliyat imkoniyatlari bormi?",
        "Magistratura dasturlari mavjudmi?",
        "Xalqaro hamkorlik dasturlari qanday?",
        "Bitiruvchilar diplomi qayerda tan olinadi?",
        "O'qituvchilar malakasi qanday?",
        "Laboratoriya va texnik jihozlar holati qanday?",
        "Talabalar uchun qo'shimcha kurslar tashkil qilinadimi?",
        "Amaliyot o'tash imkoniyatlari qanday?",
        "Talabalar uyushmasi faoliyati qanday?",
        "Masofaviy ta'lim imkoniyatlari mavjudmi?"
    ]))
    
    answer = LazyFunction(lambda: fake.text(max_nb_chars=200))
    is_active = LazyFunction(lambda: random.choice([True, True, True, False]))  # 75% faol
    order = Sequence(lambda n: n)
