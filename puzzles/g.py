from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class StackValue:
    value: int
    local_max: int


class StackMaxEffective:
    def __init__(self):
        self.state: List[StackValue] = []

    @property
    def local_max(self) -> Optional[int]:
        if self.state:
            return self.state[-1].local_max

    def push(self, value: int) -> None:
        local_max = self.local_max
        if local_max is None or value > local_max:
            local_max = value

        stack_value = StackValue(
            value=value,
            local_max=local_max,
        )
        self.state.append(stack_value)

    def pop(self, *args: int) -> Optional[str]:
        if not self.state:
            return 'error'
        self.state.pop()

    def get_max(self, *args: int) -> Union[str, int]:
        if self.local_max is None:
            return 'None'
        return self.local_max


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
