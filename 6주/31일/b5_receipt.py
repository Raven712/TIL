import sys
input = sys.stdin.readline

X = int(input()) #영수증금액
N = int(input()) #물건수
sum_ = 0
for i in range(N):
    a, b = map(int,input().split())
    sum_ += a * b
if sum_ == X:
    print('Yes')
else:
    print('No')