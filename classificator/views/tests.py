from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from views.views import *
from views.models import Infrerence
from model.models import Image
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your tests here.
#Testing Views
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.image_url = reverse('image', args=['1'])

    # def tearDown(self):
    #     logout()

    def test_home_page_view_GET_not_logged_in(self):
        responce = self.client.get(self.home_url)
        self.assertEquals(responce.status_code, 302)

    # def test_home_page_view_GET_logged_in(self):
    #     request = self.client.get(self.home_url)
    #     username, password = 'user1', 'password'
    #     user = User.objects.create_user(username, password=password)
    #     user.save()
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user=user)

    def test_image_view_GET_not_exists(self):
        responce = self.client.get(self.image_url)
        self.assertEquals(responce.status_code, 404)

    def test_image_view_GET_exists(self):
        Image.objects.create(image='./media/images/image/bird.jpg')
        responce = self.client.get(self.image_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='image.html')




#URL tests
class TestUrls(SimpleTestCase):
    def test_image_url_is_resolved(self):
        url = reverse('image', args=['1'])
        self.assertEquals(resolve(url).func, view_image)
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page)
    def test_update_url_is_resolved(self):
        url = reverse('update', args=['1'])
        self.assertEquals(resolve(url).func, update_image)
    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=['1'])
        self.assertEquals(resolve(url).func, delete_image)
    def test_infer_url_is_resolved(self):
        url = reverse('infer', args=['1'])
        self.assertEquals(resolve(url).func, run_inference)