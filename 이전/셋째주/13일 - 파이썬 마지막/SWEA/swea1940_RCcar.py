import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    v = 0
    l = 0
    for i in range(N):
        c = list(map(int, input().split()))
        if c[0] == 0:
            v = v
            l = l + v
        if c[0] == 1:
            v = v + c[1]
            l = l + v
        if c[0] == 2:
            if abs(c[1]) > v:
                v = 0
            else:
                v = v - c[1]
                l = l + v
    print(f'#{test_case} {l}')





## 문제 이해가 안됨 << T= int(input()) 때문에 헷갈렸음............
