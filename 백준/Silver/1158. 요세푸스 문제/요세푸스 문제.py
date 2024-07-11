import sys
from collections import deque

N, K = map(int, input().split())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)
answer = []

while queue:
    for i in range(1, K):
        queue.append(queue.popleft())  # pop하고 바로 다시 연결한다
    answer.append(queue.popleft())  # K번째 원소는 리스트에 추가한다

# join()메서드를 이용하려면 정수형 요소들을 문자열로 변경해야한다
print("<", ", ".join(map(str, answer)), ">", sep="")
