import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with regular list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # Test with regular list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Test with mixed list of positive and negative integers
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        # Test with list of all zeros
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        # Test with empty list
        self.assertIsNone(max_integer([]))
        # Test with list of one element
        self.assertEqual(max_integer([5]), 5)
        # Test with list of repeated elements
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        # Test with list of floating point numbers
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

if __name__ == '__main__':
    unittest.main()
