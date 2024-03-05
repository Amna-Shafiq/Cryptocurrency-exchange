from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ExchangeRateAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_valid_request(self):
        #Adjust the URL in self.client.get() according to your project's URL configuration, I have used my local host
        response = self.client.get('http://127.0.0.1:8000/exchange-routing/?amount=500')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('best_price', response.data)

    def test_amount_less_than_zero(self):
        response = self.client.get('http://127.0.0.1:8000/exchange-routing/?amount=-1')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_amount_invalid_non_numeric(self):
        response = self.client.get('http://127.0.0.1:8000/exchange-routing/?amount="hey-amna"')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_non_existent_endpoint(self):
        response = self.client.get('http://127.0.0.1:8000/non-existent-endpoint/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
