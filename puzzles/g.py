class StackMaxEffective:
    def __init__(self):
        self.max_elem = None
        self.stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.max_elem or value > self.max_elem:
            self.max_elem = value

    def pop(self, *args):
        if not self.stack:
            return 'error'

        self.max_elem = None
        self.stack.pop()

    def get_max(self, *args):
        if self.stack and self.max_elem is None:
            self.max_elem = max(self.stack)
        return 'None' if self.max_elem is None else self.max_elem


if __name__ == '__main__':
    input_length = int(input())
    stack = StackMaxEffective()

    for _ in range(input_length):
        cmd, *value = input().split()
        value = [int(v) for v in value]

        method = getattr(stack, cmd)
        result = method(*value)
        if result:
            print(result)
