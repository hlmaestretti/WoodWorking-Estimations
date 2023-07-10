"""
This file contains various unit tests for the main functionality of the program
"""

import unittest
import canFit
import Board
import woodCutEstimate
import random


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

    def test_Board(self):
        """
        This tests whether the Board class functions properly
        """
        b1 = Board.Board(3, 2, 1)
        b2 = Board.Board(2, 1, 1)
        b3 = Board.Board(4, 1, 1)
        b4 = Board.Board(1, 4, 1)
        b5 = Board.Board(1, 1, 4)

        # Test Area and Volume calculations
        self.assertEqual(6.0, b1.get_area())
        self.assertEqual(6.0, b1.get_volume())

        # Test canFit
        self.assertTrue(b1.can_fit(b2))
        self.assertFalse(b1.can_fit(b3))
        self.assertFalse(b1.can_fit(b4))
        self.assertFalse(b1.can_fit(b5))

        # Test shift_board
        length = b1.get_length()
        width = b1.get_width()
        b1.shift_board()

        self.assertEqual(length, b1.get_width())
        self.assertEqual(width, b1.get_length())

        # Test canFit with board_shift
        self.assertTrue(b1.can_fit(b2))
        self.assertFalse(b1.can_fit(b3))
        self.assertFalse(b1.can_fit(b4))
        self.assertFalse(b1.can_fit(b5))

    def test_woodCutEstimate(self):
        """
        This tests the functionality of the woodCutEstimate function
        """
        list1 = [(11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1), (11.5, 1, 1)]

        self.assertEqual(13.25, woodCutEstimate.woodCutEstimate(14, 1, list1))

        list2 = []
        cut_length = 0
        for i in range(random.randint(1, 100)):
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            list2.append((x, y, 1))
            cut_length += (x+y)

        feed_rate = 14
        load_time = 1
        self.assertEquals(cut_length/feed_rate+load_time*len(list2),
                          woodCutEstimate.woodCutEstimate(feed_rate, load_time, list2 ))
