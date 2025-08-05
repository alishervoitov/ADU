from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.blog.models import InteractiveService


class InteractiveServiceListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('blog:interactive_service_list')

    def test_list_interactive_services(self):
        InteractiveService.objects.create(name='Service 1', is_active=True, order=1)
        InteractiveService.objects.create(name='Service 2', is_active=True, order=2)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_list_interactive_services_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
