import unittest
from program import sort_string_by_frequency

class TestSortStringByFrequency(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(sort_string_by_frequency(''), '')
    
    def test_single_char_string(self):
        self.assertEqual(sort_string_by_frequency('a'), 'a')
    
    def test_sorted_string(self):
        self.assertEqual(sort_string_by_frequency('aaabbbccc'), 'cccbbbaaa')
    
    def test_unsorted_string(self):
        self.assertEqual(sort_string_by_frequency('cbacba'), 'bbccaaa')
    
    def test_mixed_case_string(self):
        self.assertEqual(sort_string_by_frequency('aAAbBbcC'), 'AAAbbBCCcc')
    
    def test_whitespace_string(self):
        self.assertEqual(sort_string_by_frequency('hello world'), 'llloohe wrd')

if __name__ == '__main__':
    unittest.main()