from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_user_creation(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'newuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_update(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('user_update', args=[self.user.pk]), {
            'username': 'updateduser',
            'email': 'updated@example.com',
        })
        self.assertRedirects(response, reverse('user_list'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_deletion(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('user_delete', args=[self.user.pk]))
        self.assertRedirects(response, reverse('user_list'))
        self.assertFalse(User.objects.filter(username='testuser').exists())
