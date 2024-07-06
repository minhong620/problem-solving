n = int(input())
stack = []
operator = []
count = 1
flag = 0
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        operator.append('+')
        count += 1

    if stack[-1] == num:  # stack의 top이 입력한 숫자와 같다면
        stack.pop()
        operator.append('-')

    else:  # stack의 top이 입력한 숫자와 다르다면
        print("NO")
        flag = 1
        break

if flag == 0:
    for op in operator:
        print(op)
