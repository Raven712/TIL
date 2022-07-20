a = '#'
b = '+'
n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print(a, end = '')
        else:
            print(b, end = '')
        if j == 4:
            if i != 4:
                print('')
            else:
                pass