from django.test import TestCase
from django.contrib.auth.models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            first_name='test_fn_1',
            last_name='test_ln_1',
            username='test_un_1'
        )

    def test_user_create(self):
        self.assertEquals(self.user1.username, 'test_un_1')
        self.assertEquals(self.user1.first_name, 'test_fn_1')
        self.assertEquals(self.user1.last_name, 'test_ln_1')
