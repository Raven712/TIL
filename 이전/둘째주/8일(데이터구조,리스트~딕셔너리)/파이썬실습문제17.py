a = list(input())
b = 0
c = 0
for i in range(len(a)):
    if 122 >= ord(a[i]) >= 97:
        b = ord(a[i]) - 32
        print(chr(b), end = '')
    else:
        c = ord(a[i])
        print(chr(c), end = '')
    