import sys

T = int(input())
for _ in range(T):
    test = sys.stdin.readline().strip()
    stack = []
    for t in test:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if len(stack) != 0:
                stack.pop()
            else:  # stack에 '(' 없을 경우
                print("NO")
                break
    else:  # 파이썬에는 for-else문이 존재
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
