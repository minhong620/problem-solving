N = int(input())
i = 2
while N > 1:
    if N % i == 0:
        print(i)
        N = N // i  # 나누기의 결과가 int
    else:
        i += 1
