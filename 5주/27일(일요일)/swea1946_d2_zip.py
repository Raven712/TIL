T = int(input())
for i in range(1, T + 1):
    N = int(input())
    print(f'#{i}')
    count = 0
    Ai = ''
    for j in range(N):
        Ci, Ki = input().split()
        Ai += Ci * int(Ki)
        
    for j in range(len(Ai)):
        if j != 0 and j % 10 == 0:
            print()
        print(Ai[j], end = '')
        
    print()