# Program 1: Sort the string According to the frequency of character

Write a program to sort a string according to the frequency of character and return the final string.

### samples
Input | output
 ------|-------
hello world | llloohe wrd
tree | eetr


### Tasks
- Develop the sort algorithm using your choice of programming language
- Create test script covering all scenarios (min 5 test cases)

// Program Code.

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