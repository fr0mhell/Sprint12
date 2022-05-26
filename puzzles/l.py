def fibonacci(n):
    if n in (0, 1):
        return 1
    previous, result = 1, 1
    for _ in range(2, n + 1):
        previous, result = result, previous + result
    return result


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    result = fibonacci(n)
    print(result % 10 ** k)
