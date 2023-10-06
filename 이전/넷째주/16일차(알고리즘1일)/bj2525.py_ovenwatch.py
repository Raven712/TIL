A, B = map(int,input().split())
0 <= A <= 23
0 <= B <= 59
C = int(input())
0 <= C <= 1000


while B+C >= 60:
    B = B - 60
    A = A + 1
    while A >= 24:
        A = A - 24

print(f'{A} {B+C}')
