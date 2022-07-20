A, B = map(int, input().split())
S = 1
R = 2
P = 3
if A == S:
    if B == R:
        print('B')
    else:
        print('A')
if A == R:
    if B == S:
        print('A')
    else:
        print('B')
if A == P:
    if B == S:
        print('B')
    else:
        print('A')
