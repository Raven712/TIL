a, b = map(int, input().split())
for i in range(4):
    if i == 0:
        print(a+b)
    if i == 1:
        print(a-b)
    if i == 2:
        print(a*b)
    if i == 3:
        print(int(a/b))