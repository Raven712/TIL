T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
total = 0
for test_case in range(1, T + 1):
    a = int(input())
    for i in range(1, a + 1):
        if i % 2 == 1:
            total = total + i
        else:
            total = total - i
    print(f'#{test_case} {total}')
    total = 0    