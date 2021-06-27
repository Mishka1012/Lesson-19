from django.test import TestCase
from django.contrib.auth.models import User
from userflow.models import Profile


class TestModels(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='user1',
            password='password'
        )
        self.profile = Profile.objects.create(
            user= self.user
        )

    # def test_user_name_assigned(self):
    #     self.assertEquals(self.profile.attached_user_id, self.user.id)
