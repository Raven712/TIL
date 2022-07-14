a = ord(input())
b = ord('a')
while a >= b:
    print(chr(b), end = ' ')
    b = b+1
    if a == b:
        print(chr(a), end = ' ')
        break
