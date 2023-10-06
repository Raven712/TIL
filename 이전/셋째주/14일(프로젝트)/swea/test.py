T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    L = []
    a = 50000

    x = 0
    for i in range(len(str(N))):
        x = N // a 
        L.append(x)
        N = N - (a * x)
        if i % 2 == 0:
            a = a / 5
        else:
            a = a / 2
    #if N != 0:

    print(L)