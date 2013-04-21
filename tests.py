from adjacent_digits import has_adjacent_digits
import unittest

class test_binary_digits(unittest.TestCase):
    def test_adjacent_digits(self):
        self.assertFalse(has_adjacent_digits('10'))
        self.assertTrue(has_adjacent_digits('11'))




