T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    if W <= R:
        if P*W <= Q:
            print(f'#{test_case} {P*W}')
        else:
            print(f'#{test_case} {Q}')
    else:
        if P * W <= (Q + (W - R) * S):
            print(f'#{test_case} {P*W}')
        else:
            print(f'#{test_case} {Q + (W - R) * S}')