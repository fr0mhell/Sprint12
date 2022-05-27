from typing import List


class Queue:

    def __init__(self):
        self.queue: List[int] = []

    def get(self, *args: int):
        if not self.queue:
            return 'error'
        return self.queue.pop(0)

    def put(self, x):
        self.queue.append(x)

    def size(self, *args: int):
        return len(self.queue)


if __name__ == '__main__':
    input_length = int(input())
    queue = Queue()

    for _ in range(input_length):
        cmd, *value = input().split()
        value = [int(v) for v in value]

        method = getattr(queue, cmd)
        result = method(*value)
        if result is not None:
            print(result)
