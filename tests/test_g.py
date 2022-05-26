from unittest import TestCase

from puzzles.g import StackMaxEffective
from utils import get_clean_values


class PuzzleGTestCase(TestCase):

    def setUp(self) -> None:
        self.stack = StackMaxEffective()

    def common_test(self, input_values, expected_states):
        for order, inp in enumerate(input_values):
            command, *value = inp.split()
            value = [int(v) for v in value]
            method = getattr(self.stack, command)

            with self.subTest(f'{order + 1}. {inp}'):
                result = method(*value)

                expected_local_max, expected_stack, expected_output = expected_states[order]

                local_max = [s.local_max for s in self.stack.state]
                stack_state = [s.value for s in self.stack.state]
                self.assertListEqual(local_max, expected_local_max)
                self.assertListEqual(stack_state, expected_stack)
                self.assertEqual(result, expected_output)

    def test_4(self):
        raw_input = """
        get_max
        push -7
        pop
        get_max
        pop
        push 2
        get_max
        pop
        get_max
        push 7
        push -5
        pop
        push -6
        pop
        get_max
        pop
        get_max
        get_max
        pop
        push -4
        push 10
        push -8
        push -6
        push -10
        push 0
        pop
        push 7
        get_max
        push 3
        push -10
        get_max
        """
        input_values = get_clean_values(raw_input)
        expected_states = [
            ([], [], 'None'),
            ([-7], [-7], None),
            ([], [], None),
            ([], [], 'None'),
            ([], [], 'error'),
            ([2], [2], None),
            ([2], [2], 2),
            ([], [], None),
            ([], [], 'None'),
            ([7], [7], None),
            ([7, 7], [7, -5], None),
            ([7], [7], None),
            ([7, 7], [7, -6], None),
            ([7], [7], None),
            ([7], [7], 7),
            ([], [], None),
            ([], [], 'None'),
            ([], [], 'None'),
            ([], [], 'error'),
            ([-4], [-4], None),
            ([-4, 10], [-4, 10], None),
            ([-4, 10, 10], [-4, 10, -8], None),
            ([-4, 10, 10, 10], [-4, 10, -8, -6], None),
            ([-4, 10, 10, 10, 10], [-4, 10, -8, -6, -10], None),
            ([-4, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 0], None),
            ([-4, 10, 10, 10, 10], [-4, 10, -8, -6, -10], None),
            ([-4, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 7], None),
            ([-4, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 7], 10),
            ([-4, 10, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 7, 3], None),
            ([-4, 10, 10, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 7, 3, -10], None),
            ([-4, 10, 10, 10, 10, 10, 10, 10], [-4, 10, -8, -6, -10, 7, 3, -10], 10),
        ]

        self.common_test(input_values, expected_states)

    def test_zero(self):
        input_values = [
            'push 0',
            'push 1',
            'get_max',
            'get_max',
            'pop',
            'get_max',
        ]
        expected_states = [
            ([0], [0], None),
            ([0, 1], [0, 1], None),
            ([0, 1], [0, 1], 1),
            ([0, 1], [0, 1], 1),
            ([0], [0], None),
            ([0], [0], 0),
        ]

        self.common_test(input_values, expected_states)

    def test_7(self):
        raw_input = """
get_max
pop
push -7
pop
get_max
get_max
get_max
get_max
push 1
get_max
get_max
push 3
pop
pop
get_max
get_max
get_max
push -3
get_max
get_max
push 0
push 9
get_max
get_max
pop
get_max
push 4
        """
        input_values = get_clean_values(raw_input)
        expected_states = [
            ([], [], 'None'),
            ([], [], 'error'),
            ([-7], [-7], None),
            ([], [], None),
            ([], [], 'None'),
            ([], [], 'None'),
            ([], [], 'None'),
            ([], [], 'None'),
            ([1], [1], None),
            ([1], [1], 1),
            ([1], [1], 1),
            ([1, 3], [1, 3], None),
            ([1], [1], None),
            ([], [], None),
            ([], [], 'None'),
            ([], [], 'None'),
            ([], [], 'None'),
            ([-3], [-3], None),
            ([-3], [-3], -3),
            ([-3], [-3], -3),
            ([-3, 0], [-3, 0], None),
            ([-3, 0, 9], [-3, 0, 9], None),
            ([-3, 0, 9], [-3, 0, 9], 9),
            ([-3, 0, 9], [-3, 0, 9], 9),
            ([-3, 0], [-3, 0], None),
            ([-3, 0], [-3, 0], 0),
            ([-3, 0, 4], [-3, 0, 4], None),
        ]

        self.common_test(input_values, expected_states)
