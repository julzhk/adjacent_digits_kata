from adjacent_digits import (has_adjacent_digits, generate_binary)
import unittest

class test_binary_digits(unittest.TestCase):
    def test_adjacent_digits(self):
        self.assertFalse(has_adjacent_digits('10'))
        self.assertTrue(has_adjacent_digits('11'))
        self.assertTrue(has_adjacent_digits('0110'))
        self.assertFalse(has_adjacent_digits('00'))
        self.assertFalse(has_adjacent_digits('0'))

    def test_create_binary_digits_from_decimal(self):
        self.assertEqual(generate_binary(1),'1')




