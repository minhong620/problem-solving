N = int(input())
coordinate_list = []

for _ in range(N):
    coordinate = list(map(int, input().split()))
    coordinate_list.append(coordinate)
coordinate_list.sort()

for coordinate in coordinate_list:
    print(coordinate[0], coordinate[1])
