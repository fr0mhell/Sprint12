from functools import lru_cache
import sys


class RecursionDepthContext:

    def __init__(self, new_limit):
        self._system_limit = sys.getrecursionlimit()
        self._new_limit = new_limit

    def __enter__(self):
        if self._new_limit > self._system_limit:
            sys.setrecursionlimit(self._new_limit)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.setrecursionlimit(self._system_limit)


@lru_cache(maxsize=3)
def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    with RecursionDepthContext(3 * n):
        result = fibonacci(n)
    print(result % 10 ** k)
