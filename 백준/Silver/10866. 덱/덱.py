import sys
from collections import deque

N = int(input())
deque = deque()

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.appendleft(command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
