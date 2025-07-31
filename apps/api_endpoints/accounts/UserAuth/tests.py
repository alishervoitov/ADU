from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from apps.users.factories import UserFactory

class JWTAuthenticationTestCase(APITestCase):
    """JWT Authentication uchun testlar"""
    
    def setUp(self):
        """Har bir test metodidan oldin ishlaydigan setup"""
        self.client = APIClient()
        
        # Test foydalanuvchisini Factory orqali yaratish
        self.user = UserFactory(
            username='testuser',
            email='test@example.com'
        )
        
        # URL nomlarini sozlash
        self.token_obtain_url = reverse('users-api:token_obtain_pair')
        self.token_refresh_url = reverse('users-api:token_refresh')
        
    def test_token_obtain_with_valid_credentials(self):
        """To'g'ri login ma'lumotlari bilan token olish testi"""
        data = {
            'username': 'testuser',
            'password': 'defaultpass123'
        }
        
        response = self.client.post(self.token_obtain_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        
        # Token formatini tekshirish
        access_token = response.data['access']
        refresh_token = response.data['refresh']
        
        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)
        self.assertTrue(len(access_token) > 100)  
        self.assertTrue(len(refresh_token) > 100)
        
    def test_token_obtain_with_invalid_credentials(self):
        """Noto'g'ri login ma'lumotlari bilan token olish testi"""
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        
        response = self.client.post(self.token_obtain_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)
        self.assertNotIn('refresh', response.data)
        
    def test_token_refresh_with_valid_token(self):
        """To'g'ri refresh token bilan yangi access token olish testi"""
        data = {
            'username': 'testuser',
            'password': 'defaultpass123'
        }
        response = self.client.post(self.token_obtain_url, data, format='json')
        refresh_token = response.data['refresh']
        

        refresh_data = {'refresh': refresh_token}
        response = self.client.post(self.token_refresh_url, refresh_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        
        new_access_token = response.data['access']
        self.assertIsInstance(new_access_token, str)
        self.assertTrue(len(new_access_token) > 100)