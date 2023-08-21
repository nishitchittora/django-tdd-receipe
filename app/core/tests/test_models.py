from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from decimal import Decimal


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

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', "test123")

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_receipe(self):
        user = get_user_model().objects.create_user("test@gmail.com", "password321")
        receipe = models.Recipe.objects.create(
            user=user,
            title="test",
            time_minutes=5,
            price=Decimal("5.5"),
            description="Test description"
        )
        self.assertEqual(str(receipe), receipe.title)
