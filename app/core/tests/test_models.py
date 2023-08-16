from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "password321"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        samples_email = [
            ("test3@GMAIL.com", "test3@gmail.com"),
            ("Test4@GMAIL.com", "Test4@gmail.com"),
            ("Test5@GMAIL.com", "Test5@gmail.com"),
            ("test6@GMAIL.COM", "test6@gmail.com"),
        ]

        for email, expected in samples_email:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)
