croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatia:
    word = word.replace(i, "*")  # 같은 이름의 변수를 설정해야 초기화되지 않음(replace함수가 비파괴적이기 때문에)

print(len(word))
