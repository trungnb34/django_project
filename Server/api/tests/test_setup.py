from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")
        self.user_data = {
            'email' : 'test_case@gmail.com',
            'name' : "test_case",
            'password' : "123456a@"
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()