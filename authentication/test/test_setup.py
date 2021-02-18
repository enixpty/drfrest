from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('auth:register')
        self.login_url = reverse('auth:login')
        
        self.user_data = {
            'email' : 'email@gmail.com',
            'first_name' : 'test',
            'last_name' : 'test2',
            'username' : 'email',
            'password' : 'C4223YlMC45'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()