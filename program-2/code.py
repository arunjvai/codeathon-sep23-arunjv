import unittest
from program import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_profit([]), -1)
    
    def test_single_element_list(self):
        self.assertEqual(max_profit([1]), -1)
    
    def test_sorted_list(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
    
    def test_unsorted_list(self):
        self.assertEqual(max_profit([5, 4, 3, 2, 1]), -1)
    
    def test_increasing_list(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
    
    def test_decreasing_list(self):
        self.assertEqual(max_profit([9, 8, 7, 6, 5, 4, 3, 2, 1]), -1)

if __name__ == '__main__':
    unittest.main()