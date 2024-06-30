a = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
b = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
result = 0  # 학점 x 과목평점
total = 0  # 학점의 총점

for i in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)  # 문자열로 입력되어서 float으로 변환
    if grade != "P":
        idx = a.index(grade)
        grade = b[idx]
        result += credit * grade
        total += credit

print(result / total)
