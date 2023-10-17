word = input()
count = 0

for i in range(len(word)):
    if word[i] == '-':
        pass
    elif word[i] == '=':
        if i >= 2 and word[i - 2] == 'd' and word[i - 1] == 'z':
            count -= 1
        else:
            pass
    elif word[i] == 'j':
        if i >= 1 and word[i - 1] == 'l':      #여기서 에러가 납니다                   
            pass
        elif i >= 1 and word[i - 1] == 'n':
            pass
        else:
            count += 1
    else:
        count += 1
print(count)