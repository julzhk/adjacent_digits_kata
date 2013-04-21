from adjacent_digits import (has_adjacent_digits, generate_binary_string,
                             count_non_adjacent_digits)
import unittest

class test_binary_digits(unittest.TestCase):
    def test_adjacent_digits(self):
        self.assertFalse(has_adjacent_digits('10'))
        self.assertTrue(has_adjacent_digits('11'))
        self.assertTrue(has_adjacent_digits('0110'))
        self.assertFalse(has_adjacent_digits('00'))
        self.assertFalse(has_adjacent_digits('0'))

    def test_create_binary_digits_from_decimal(self):
        self.assertEqual(generate_binary_string(1),'1')
        self.assertEqual(generate_binary_string(2), '10')
        self.assertEqual(generate_binary_string(3), '11')

    def test_count_number_non_adjacent_binary_digits(self):
        self.assertEqual(count_non_adjacent_digits(1),1)




