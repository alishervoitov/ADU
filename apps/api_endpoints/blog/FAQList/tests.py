from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.blog.models import FAQ
from apps.blog.factories import FAQFactory
from apps.users.models import User


class FAQListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('blog:faq_list')
        
        # Test uchun admin user yaratish
        self.admin_user = User.objects.create_user(
            username='testadmin',
            email='admin@test.com',
            password='testpass123',
            is_staff=True,
            is_superuser=True
        )

    def test_list_faqs(self):
        """FAQ ro'yxatini olish testi"""
        # Test FAQ lar yaratish
        faq1 = FAQFactory(
            question="Test savol 1",
            answer="Test javob 1",
            is_active=True,
            order=1
        )
        faq2 = FAQFactory(
            question="Test savol 2", 
            answer="Test javob 2",
            is_active=True,
            order=2
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
        # Ma'lumotlarni tekshirish
        self.assertEqual(response.data[0]['question'], "Test savol 1")
        self.assertEqual(response.data[0]['answer'], "Test javob 1")

    def test_list_faqs_empty(self):
        """Bo'sh FAQ ro'yxati testi"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_list_only_active_faqs(self):
        """Faqat faol FAQ larni olish testi"""
        # Faol FAQ
        active_faq = FAQFactory(
            question="Faol savol",
            answer="Faol javob",
            is_active=True,
            order=1
        )
        
        # Nofaol FAQ
        inactive_faq = FAQFactory(
            question="Nofaol savol",
            answer="Nofaol javob", 
            is_active=False,
            order=2
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "Faol savol")

    def test_faq_ordering(self):
        """FAQ larning tartib bo'yicha qaytarilishini tekshirish"""
        # Tartibni buzmay yaratish
        faq3 = FAQFactory(
            question="Uchinchi savol",
            answer="Uchinchi javob",
            is_active=True,
            order=3
        )
        
        faq1 = FAQFactory(
            question="Birinchi savol",
            answer="Birinchi javob", 
            is_active=True,
            order=1
        )
        
        faq2 = FAQFactory(
            question="Ikkinchi savol",
            answer="Ikkinchi javob",
            is_active=True,
            order=2
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        
        # Tartibni tekshirish
        self.assertEqual(response.data[0]['question'], "Birinchi savol")
        self.assertEqual(response.data[1]['question'], "Ikkinchi savol")
        self.assertEqual(response.data[2]['question'], "Uchinchi savol")

    def test_faq_fields(self):
        """FAQ serializer maydonlarini tekshirish"""
        faq = FAQFactory(
            question="Test savol",
            answer="Test javob",
            is_active=True,
            order=1
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        
        faq_data = response.data[0]
        # Serializer da faqat question va answer maydonlari bo'lishi kerak
        expected_fields = ['question', 'answer']
        self.assertEqual(list(faq_data.keys()), expected_fields)

    def test_api_without_pagination(self):
        """Paginationsiz API testi"""
        # Ko'p FAQ yaratish
        for i in range(25):  # Default pagination dan ko'proq
            FAQFactory(
                question=f"Savol {i+1}",
                answer=f"Javob {i+1}",
                is_active=True,
                order=i+1
            )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Barcha FAQ lar qaytarilishi kerak (pagination yo'q)
        self.assertEqual(len(response.data), 25)
        # Pagination kalitlari bo'lmasligi kerak
        self.assertNotIn('count', response.data)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)