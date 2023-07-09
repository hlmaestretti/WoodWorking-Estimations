"""
This file contains various unit tests for the main functionality of the program
"""

import unittest
import canFit

class TestVariousFunctions(unittest.TestCase):

    def test_canFit(self):
        """
        This tests whether canFit functions properly
        """
        list_cuts = [(11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (40, .75, 1)]
        list_boards = [(48, 9, 1)]

        test = canFit.canFit(list_cuts, list_boards, .125)
        self.assertIsInstance(test, list, "Test 1 passed")

        list_cuts = [(11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1),
                     (40, .75, 1)]
        list_boards = [(47, 3, 1)]
        test = canFit.canFit(list_cuts, list_boards, .125)
        self.assertFalse(test, "Test 2 passed")

        list_cuts = [(47, 3, 1)]
        list_boards = [(47, 3, 1)]
        test = canFit.canFit(list_cuts, list_boards, .125)
        self.assertIsInstance(test, list, "Test 3 passed")

