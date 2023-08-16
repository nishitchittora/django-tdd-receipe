from django.test import SimpleTestCase

from .cal import add


class CalcTest(SimpleTestCase):
    def test_add_number(self):
        res = add(5, 6)
        self.assertEqual(res, 11)
