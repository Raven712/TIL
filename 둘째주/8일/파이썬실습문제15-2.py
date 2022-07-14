word = input()
cnt = 0
if 'a' in word:
    for words in range(len(word)):
        if word[words] == 'a':
            print(words,end=' ')
else:
    print(-1)

#베낌