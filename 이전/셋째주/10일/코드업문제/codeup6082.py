a = int(input())
for i in range(1, a+1):
    if i % 10 == 3:
        i = 'X'
    elif i % 10 == 6:
        i = 'X'
    elif i % 10 == 9:
        i = 'X'
    print(i, end=' ')