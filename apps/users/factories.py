import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()

User = get_user_model()


class UserFactory(DjangoModelFactory):
    """User model uchun Factory"""
    
    class Meta:
        model = User
        django_get_or_create = ('username',)  
    
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    
    password = factory.PostGenerationMethodCall('set_password', 'defaultpass123')
    
    is_active = True
    is_staff = False
    is_superuser = False
    
    date_joined = factory.Faker('date_time_this_year', tzinfo=factory.Faker('pytimezone'))
