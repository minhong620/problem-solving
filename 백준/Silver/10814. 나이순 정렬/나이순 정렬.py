import sys
import math

N = int(sys.stdin.readline())
member_list = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    member_list.append([int(age), name])

# lambda 함수를 사용하여 첫번째 요소(나이)에 대해서만 정렬한다
member_list.sort(key=lambda x: x[0])

for member in member_list:
    print(member[0], member[1])
