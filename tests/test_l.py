from unittest import TestCase

from puzzles.l import fibonacci


class PuzzleLTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    def test_fibonacci(self):
        for n, expected in enumerate(self.expected):
            with self.subTest(n=n, expected=expected):
                self.assertEqual(fibonacci(n, 10 ** 3), expected)
