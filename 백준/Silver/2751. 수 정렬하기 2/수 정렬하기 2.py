import sys

N = int(input())
num_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()
for num in num_list:
    print(num)
