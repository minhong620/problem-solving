N = int(input())
flag = 0

for i in range(1, N + 1):
    # 문자열로 변환 후 map()함수를 이용해서 정수형 리스트로 만들고 합해서 각 자리수의 합을 알아낸다
    num = sum(map(int, str(i)))
    result = i + num

    if result == N:
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)
