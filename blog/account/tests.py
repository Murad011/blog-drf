from rest_framework.test import APITestCase
from django.urls import reverse


class UserRegistertrationTestCase(APITestCase):
    url = reverse("account:register")


    def test_user_registration(self):

        data = {
            "username":"oguzhantest",
            "password": "deneme123"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201,response.status_code)



    def test_user_invalid_password(self):
        """
        invalid password datasi ile register islemi
        """

        data = {
            "username":"oguzhantest",
            "password": "1"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400,response.status_code)