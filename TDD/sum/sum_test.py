import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

    def setUp(self):
        self.numbers = [10, 5, 7, 8, 90, 60]
    
    def test_sum_of_digits(self):
        '''
        Test sum of digits/numbers
        '''

        self.assertEqual(my_sum(10, 5), 15)

    def test_non_numbers(self):
        pass

if __name__ == '__main__':
    unittest.main()
