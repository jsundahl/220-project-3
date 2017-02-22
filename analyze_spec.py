import unittest
from analyze import *


class AnalyzeSpec(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(flatten([1, [2, 3, 4], [5, 6], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_difference(self):
        self.assertEqual(difference([1, 2, 3], [1, 2, 4]), [3, 4])


if __name__ == '__main__':
    unittest.main()
