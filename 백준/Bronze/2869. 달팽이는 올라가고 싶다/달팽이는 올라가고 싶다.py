# 하루에 올라가는 거리 = A - B
# 올라가야할 거리 = V - B
import math

A, B, V = map(int, input().split())

day = (V - B) / (A - B)
print(math.ceil(day))
