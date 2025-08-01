from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.utils.translation import activate, deactivate
from rest_framework.request import Request
from apps.common.models import FrontendTranslation
from apps.api_endpoints.common.FrontendTranslations.serializers import FrontendTranslationSerializer

User = get_user_model()


class LanguageAwareSerializerTest(TestCase):
    """Language-aware serializer testlari"""

    def setUp(self):
        """Test ma'lumotlarini tayyorlash"""
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Test translation'larini yaratish
        self.translations = [
            FrontendTranslation.objects.create(
                key='home_uz',
                text='Bosh sahifa',
                created_by=self.user,
                updated_by=self.user
            ),
            FrontendTranslation.objects.create(
                key='home_ru',
                text='Главная страница',
                created_by=self.user,
                updated_by=self.user
            ),
            FrontendTranslation.objects.create(
                key='home_en',
                text='Home Page',
                created_by=self.user,
                updated_by=self.user
            )
        ]

    def test_serializer_with_uzbek_context(self):
        """Uzbek til konteksti bilan serializer"""
        # Uzbek tilini aktivlashtirish
        activate('uz')
        
        uz_translation = self.translations[0]  # home_uz
        serializer = FrontendTranslationSerializer(uz_translation)
        data = serializer.data
        
        self.assertEqual(data['key'], 'home_uz')
        self.assertEqual(data['text'], 'Bosh sahifa')
        
        deactivate()

    def test_serializer_with_russian_context(self):
        """Rus til konteksti bilan serializer"""
        # Rus tilini aktivlashtirish
        activate('ru')
        
        ru_translation = self.translations[1]  # home_ru
        serializer = FrontendTranslationSerializer(ru_translation)
        data = serializer.data
        
        self.assertEqual(data['key'], 'home_ru')
        self.assertEqual(data['text'], 'Главная страница')
        
        deactivate()

    def test_serializer_with_request_language_header(self):
        """Request'dagi language header bilan serializer"""
        # Uzbek header bilan request yaratish
        request = self.factory.get('/', HTTP_ACCEPT_LANGUAGE='uz')
        drf_request = Request(request)
        
        uz_translation = self.translations[0]
        serializer = FrontendTranslationSerializer(
            uz_translation, 
            context={'request': drf_request}
        )
        data = serializer.data
        
        self.assertEqual(data['key'], 'home_uz')
        self.assertEqual(data['text'], 'Bosh sahifa')
