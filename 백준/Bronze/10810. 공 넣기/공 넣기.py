import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for num in range(i, j + 1):
        basket[num - 1] = k

for num in range(N):
    print(basket[num], end=' ')