import sys


def factorial(N):
    result = 1
    if N > 0:
        result = N * factorial(N - 1)
    return result


N = int(sys.stdin.readline())
print(factorial(N))
