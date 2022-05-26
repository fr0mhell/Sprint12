def fibonacci(n, d):
    a, b = 1, 1

    if n >= 2:
        for i in range(n-1):
            a, b = b, (a + b) % d
    return b


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    d = (10 ** k)

    print(fibonacci(n, d))
