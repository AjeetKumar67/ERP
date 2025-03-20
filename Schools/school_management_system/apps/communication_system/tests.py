from django.test import TestCase
from .models import Notification, Message

class CommunicationSystemTests(TestCase):

    def setUp(self):
        self.notification = Notification.objects.create(
            title="Test Notification",
            message="This is a test notification.",
            recipient="test@example.com"
        )
        self.message = Message.objects.create(
            sender="sender@example.com",
            recipient="recipient@example.com",
            content="This is a test message."
        )

    def test_notification_creation(self):
        self.assertEqual(self.notification.title, "Test Notification")
        self.assertEqual(self.notification.message, "This is a test notification.")
        self.assertEqual(self.notification.recipient, "test@example.com")

    def test_message_creation(self):
        self.assertEqual(self.message.sender, "sender@example.com")
        self.assertEqual(self.message.recipient, "recipient@example.com")
        self.assertEqual(self.message.content, "This is a test message.")

    def test_notification_str(self):
        self.assertEqual(str(self.notification), "Test Notification")

    def test_message_str(self):
        self.assertEqual(str(self.message), "sender@example.com to recipient@example.com: This is a test message.")