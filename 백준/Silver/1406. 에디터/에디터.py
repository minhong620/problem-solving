# 스택을 두개 이용한다
# 커서는 두개의 스택 사이에 위치한다
import sys

left = list(input())
right = []
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()
    # 커서가 맨 앞일 경우도 고려하자!
    if command[0] == 'L' and left:
        right.append(left.pop())
    # L과 D는 반대
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

# append()를 사용하면 리스트가 겹치기 때문에 extend()를 사용한다
left.extend(right[::-1])
# 문자열로 변환하여 출력한다
print(''.join(left))
