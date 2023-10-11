"""

Sample tests

"""

from django.test import SimpleTestCase

from . import calc


class calcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.sub(15, 10)

        self.assertEqual(res, 5)
