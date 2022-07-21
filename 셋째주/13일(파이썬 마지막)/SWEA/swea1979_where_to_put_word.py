T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int,input().split())

    for i in range(N):
        for j in range(N):
            
            # 너무 어려워서 보류