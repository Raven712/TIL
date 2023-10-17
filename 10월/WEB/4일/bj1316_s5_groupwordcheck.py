N = int(input())
count = 0
for i in range(N):
    word = input()
    list_ = []

    for i in range(len(word)):
        if i >= 1 and word[i] in list_ and word[i - 1] != word[i]:
            break
        list_.append(word[i])
        if i == (len(word) - 1):
            count += 1
print(count)