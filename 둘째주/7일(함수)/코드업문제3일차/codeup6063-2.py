a, b = map(int, input().split())
c = 0
if a >= b:
    c += a
    print(c)
else:
    c += b
    print(c)