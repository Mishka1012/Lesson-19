from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User



class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('login')

    def test_log_in_POST_user_valid(self):
        username, password = 'user1', 'password'
        user = User.objects.create_user(username, password=password)
        user.save()

        responce = self.client.post(self.login_url, {
            'username': username,
            'password': password
        })
        self.assertEquals(responce.status_code, 302)

    def test_log_in_POST_user_invalid(self):
        responce = self.client.post(self.login_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce,template_name='registration/login.html')