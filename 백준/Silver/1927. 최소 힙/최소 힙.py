# 최소 힙 : 부모노드의 키 값이 자식노드의 키 값보다 항상 작은 힙

import heapq
import sys

N = int(input())
heap = []
cnt = 0

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
            cnt += 1
    else:
        heapq.heappush(heap, x)
