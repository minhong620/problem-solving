import sys
import math


def func(n):
    if n <= 1:
        return n
    return func(n - 1) + func(n - 2)


n = int(sys.stdin.readline())
print(func(n))
