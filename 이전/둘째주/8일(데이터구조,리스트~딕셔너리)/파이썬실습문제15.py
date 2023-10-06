word = input()
a = 0
for i in word:
    if i == 'a':
        print(a)
        break
    else:
        a += 1
if 'a' not in word:
    print(-1)