T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
total = 0
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 1:
            total = total + i
    print(f'#{test_case}', end = ' ')
    print(total)
    total = 0