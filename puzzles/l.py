from functools import lru_cache
import sys

from memory_profiler import profile


@profile
def fibonacci(n, d):
    a, b = 1, 1

    if n >= 2:
        for i in range(n-1):
            a, b = b, (a + b) % d
    return b


@profile
def fibonacci_slow(n):
    if n in (0, 1):
        return 1
    previous, result = 1, 1
    for _ in range(2, n + 1):
        previous, result = result, previous + result
    return result


class RecursionDepthContext:

    def __init__(self, new_limit):
        self._system_limit = sys.getrecursionlimit()
        self._new_limit = new_limit

    def __enter__(self):
        if self._new_limit > self._system_limit:
            sys.setrecursionlimit(self._new_limit)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.setrecursionlimit(self._system_limit)


@profile
def fibonacci_recursive(n, d):

    @lru_cache(maxsize=None)
    def fibonacci(n, d):
        if n in (0, 1):
            return 1
        return (fibonacci(n-1, d) + fibonacci(n-2, d)) % d

    with RecursionDepthContext(3 * n):
        return fibonacci(n, d)


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    d = (10 ** k)

    print(fibonacci(n, d))
    print(fibonacci_slow(n) % d)
    print(fibonacci_recursive(n, d))
