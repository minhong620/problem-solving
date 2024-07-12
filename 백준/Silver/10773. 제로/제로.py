import sys
from collections import deque

K = int(input())
stack = []
result = 0
for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for i in stack:
    result += i

print(result)
