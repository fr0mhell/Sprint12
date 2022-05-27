from unittest import TestCase

from puzzles.j import Queue
from utils import get_clean_values


class PuzzleJTestCase(TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def common_test(self, input_values, expected_states):
        for order, inp in enumerate(input_values):
            command, *value = inp.split()
            value = [int(v) for v in value]
            method = getattr(self.queue, command)

            with self.subTest(f'{order + 1}. {inp}'):
                result = method(*value)

                expected_queue, expected_output = expected_states[order]

                self.assertListEqual(self.queue.queue, expected_queue)
                self.assertEqual(result, expected_output)

    def test_1(self):
        raw_input = """
put -34
put -23
get
size
get
size
get
get
put 80
size
        """
        input_values = get_clean_values(raw_input)
        expected_states = [
            ([-34], None),
            ([-34, -23], None),
            ([-23], -34),
            ([-23], 1),
            ([], -23),
            ([], 0),
            ([], 'error'),
            ([],  'error'),
            ([80], None),
            ([80], 1),
        ]

        self.common_test(input_values, expected_states)
