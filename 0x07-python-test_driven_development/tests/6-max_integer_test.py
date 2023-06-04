import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: List with positive integers
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)

        # Test case 2: List with positive integers in different order
        list2 = [1, 3, 4, 2]
        self.assertEqual(max_integer(list2), 4)

        # Test case 3: List with negative integers
        list3 = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list3), -1)

        # Test case 4: List with positive and negative integers
        list4 = [-1, 2, -3, 4]
        self.assertEqual(max_integer(list4), 4)

        # Test case 5: List with duplicate maximum value
        list5 = [1, 4, 4, 2]
        self.assertEqual(max_integer(list5), 4)

        # Test case 6: Empty list
        list6 = []
        self.assertIsNone(max_integer(list6))

    def test_max_integer_type(self):
        # Test case 7: List with non-integer elements
        list7 = [1, 2, "3", 4]
        with self.assertRaises(TypeError):
            max_integer(list7)

if __name__ == '__main__':
    unittest.main()
