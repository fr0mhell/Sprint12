from functools import lru_cache


@lru_cache(maxsize=3)
def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    result = fibonacci(n)
    print(result % 10 ** k)
