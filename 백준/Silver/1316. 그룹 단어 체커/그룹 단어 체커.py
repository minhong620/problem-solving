N = int(input())
for i in range(N):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            continue
        if word[j] in word[j + 1:]:
            N -= 1
            break

print(N)
