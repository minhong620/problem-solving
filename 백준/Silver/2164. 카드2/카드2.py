import sys
from collections import deque

N = int(input())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

for i in range(N - 1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
