from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models.status import Status


class StatusCRUDTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_status_creation(self):
        response = self.client.post(reverse('status_create'), {'name': 'In Progress'})
        self.assertEqual(Status.objects.count(), 1)
        self.assertEqual(Status.objects.first().name, 'In Progress')
        self.assertEqual(Status.objects.first().user, self.user)

    def test_user_can_only_see_their_statuses(self):
        status1 = Status.objects.create(name='In Progress', user=self.user)
        status2 = Status.objects.create(name='Completed', user=self.other_user)

        response = self.client.get(reverse('status_list'))
        self.assertContains(response, 'In Progress')
        self.assertNotContains(response, 'Completed')
