import sys
import math


def factorial(N):
    if N <= 1:
        answer = 1
    else:
        answer = factorial(N - 1) * N

    return answer


N = int(sys.stdin.readline())
print(factorial(N))
