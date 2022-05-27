from unittest import TestCase

from puzzles.h import parentheses_sequence


class PuzzleHTestCase(TestCase):

    def test_valid_sequence(self):
        self.assertTrue(parentheses_sequence('[{()}]'))

    def test_invalid_sequence(self):
        self.assertFalse(parentheses_sequence('[{]}'))

    def test_invalid_sequence_odd_length(self):
        self.assertFalse(parentheses_sequence('[[[]]'))
