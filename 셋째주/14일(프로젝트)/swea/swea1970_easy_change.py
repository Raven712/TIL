T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    L = []
    for i in str(N):
        L.append(i)
    L2 = []
    if N >= 50000:
        a = N // 50000
        N = N - a * 50000
        L2.append(a)
    else:
        L2.append(0)
    if 50000 > N >= 10000:
        a = N // 10000
        N = N - a * 10000
        L2.append(a)
    else:
        L2.append(0)
    if 10000 > N >= 5000:
        