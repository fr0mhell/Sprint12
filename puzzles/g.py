class StackMaxEffective:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self, *args):
        if not self.stack:
            return 'error'
        self.stack.pop()

    def get_max(self, *args):
        if not self.stack:
            return 'None'
        return max(self.stack)


if __name__ == '__main__':
    input_length = int(input())
    stack = StackMaxEffective()

    for _ in range(input_length):
        cmd, *value = input().split()
        value = [int(v) for v in value]

        method = getattr(stack, cmd)
        result = method(*value)
        if result is not None:
            print(result)
