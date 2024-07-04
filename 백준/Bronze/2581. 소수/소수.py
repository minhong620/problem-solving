M = int(input())
N = int(input())
num_list = []

for i in range(M, N + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])
