N = int(input())

cell = 1
cnt = 1
while N > cell:
    cell += 6 * cnt
    cnt += 1

print(cnt)
