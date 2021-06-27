from django.test import SimpleTestCase
from userflow.views import register_page, user_page
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register_page, msg='Register url returned wrong function!')
