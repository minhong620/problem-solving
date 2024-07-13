degree_list = []
degree_sum = 0
for _ in range(3):
    degree = int(input())
    degree_sum += degree
    degree_list.append(degree)

if degree_sum != 180:
    print("Error")
else:
    if degree_list[0] == 60 and degree_list[1] == 60:
        print("Equilateral")
    elif degree_list[0] == degree_list[1] or degree_list[1] == degree_list[2] or degree_list[2] == degree_list[0]:
        print("Isosceles")
    elif degree_list[0] != degree_list[1] and degree_list[1] != degree_list[2] and degree_list[2] != degree_list[0]:
        print("Scalene")
