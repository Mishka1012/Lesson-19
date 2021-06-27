from django.test import TestCase
from userflow.forms import CreateUserForm


class TestForms(TestCase):
    def test_registration_form_valid_data(self):
        form = CreateUserForm(data={
            'username': 'user1',
            'email': 'user@gmail.com',
            'password1': 'password1',
            'password2': 'password1'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_not_valid_data(self):
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())