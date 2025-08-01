from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.common.models import FrontendTranslation


class FrontendTranslationAPITest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('common:frontend-translations')

        self.translation = FrontendTranslation.objects.create(
            key='greeting',
            text='Salom',                 # uz
            text_uz_cyrl='Салом',         # uz-cyrl
            text_ru='Здравствуйте',       # ru
            text_en='Hello'               # en
        )

    def test_uz_translation(self):
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='uz')
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Salom')

    def test_uz_cyrl_translation(self):
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='uz-cyrl')
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Салом')

    def test_ru_translation(self):
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='ru')
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Здравствуйте')

    def test_en_translation(self):
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='en')
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Hello')

    def test_fallback_to_default_text(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Salom')

    def test_invalid_language_fallback(self):
        response = self.client.get(self.url, HTTP_ACCEPT_LANGUAGE='de')
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.data)
        self.assertEqual(response.data['greeting'], 'Salom')
