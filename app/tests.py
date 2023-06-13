from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Profile, User


class SignupViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_signup_view(self):
        url = reverse('signup')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify that a user and profile were created
        user = User.objects.get(email=data['email'])
        self.assertIsNotNone(user)
        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_login_view_with_valid_credentials(self):
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertTrue(Token.objects.filter(user=self.user).exists())

    def test_login_view_with_invalid_credentials(self):
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse('token' in response.data)
        self.assertFalse(Token.objects.filter(user=self.user).exists())


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.profile = Profile.objects.create(user=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_profile_view(self):
        url = reverse('profile')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['id'], self.profile.id)

    def test_post_profile_view_with_valid_data(self):
        url = reverse('profile')
        image_path = 'C:\\Users\\HP\\Downloads\\R.jfif'
        with open(image_path, 'rb') as image_file:
            data = {'image_test': image_file}

            response = self.client.post(url, data, format='multipart')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue('photo' in response.data)
            self.assertIsNotNone(Profile.objects.get(id=self.profile.id).photo)

    def test_post_profile_view_with_invalid_data(self):
        url = reverse('profile')
        data = {}  # Invalid data

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_)

