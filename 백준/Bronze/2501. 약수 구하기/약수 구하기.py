N, K = map(int, input().split())
num_array = []
for i in range(N):
    if N % (i + 1) == 0:
        num_array.append(i + 1)

if K > len(num_array):
    print("0")
else:
    print(num_array[K - 1])
