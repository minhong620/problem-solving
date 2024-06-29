a = input().upper()  # 대문자로 변환 후 저장(출력을 대문자로 해야해서)
b = list(set(a))  # set함수로 중복된 문자 제거 후 리스트로 변환 후 저장

c = []  # 빈 리스트 c

for i in b:  # 각각의 문자에 대하여
    counts = a.count(i)  # 문자 개수
    c.append(counts)  # c에 문자 개수 추가

if c.count(max(c)) >= 2:  # c에서 가장 큰 수가 2개 이상이면
    print("?")
else:
    print(b[c.index(max(c))])  # index함수는 원하는 값의 위치를 찾아줌
