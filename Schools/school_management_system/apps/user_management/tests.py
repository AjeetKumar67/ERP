from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagementTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email(self):
        self.user.email = 'testuser@example.com'
        self.user.save()
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_update(self):
        self.user.username = 'updateduser'
        self.user.save()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_deletion(self):
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(self.User.DoesNotExist):
            self.User.objects.get(id=user_id)