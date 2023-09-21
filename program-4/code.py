import unittest

class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(sort_array(arr), expected)
    
    def test_sort_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(sort_array(arr), expected)
    
    def test_sort_large_array(self):
        arr = list(range(50000))
        expected = list(range(50000))
        self.assertEqual(sort_array(arr), expected)

if __name__ == '__main__':
    unittest.main()

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    def sort_array(arr):
        return quicksort(arr)
    
    import timeit

    arr = list(range(50000))
    print(timeit.timeit(lambda: sort_array(arr), number=1))