import sys

T = int(input())
for _ in range(T):
    sentence = sys.stdin.readline().strip()
    sentence += ' '  # 마지막에 들어간 단어도 stack에서 꺼낼 수 있게 문장 마지막에 공백 추가
    stack = []
    for alphabet in sentence:
        if alphabet != ' ':  # 공백이 아니면
            stack.append(alphabet)  # stack에 추가
        else:  # 공백이면
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
