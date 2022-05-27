opening = {'[', '{', '('}
closing = {']', '}', ')'}
pairs = {
    '[': ']',
    '(': ')',
    '{': '}',
}


def parentheses_sequence(sequence: str) -> bool:
    parentheses_stack = []

    if len(sequence) % 2:
        return False

    for symbol in sequence:
        if symbol in opening:
            parentheses_stack.append(symbol)
            continue

        if symbol in closing:
            opening_symbol = parentheses_stack.pop()
            expected_closing = pairs.get(opening_symbol)
            if expected_closing != symbol:
                return False

    return True


if __name__ == '__main__':
    print(parentheses_sequence(input()))
