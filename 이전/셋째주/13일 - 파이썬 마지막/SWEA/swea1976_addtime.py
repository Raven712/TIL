T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, d = map(int,input().split())
    t = a + c
    m = b + d
    time = list(range(1, 13))
    min = list(range(0, 60))
    if m not in min:
        m = m - 60     # 분은 60을 넘으면 시간이 1개 늘어나고, 60을 깎으면 되니까 이렇게 했다
        t = t + 1
    if t not in time:
        t = t - 12  # 시간은 12이상이 없으니, 13시부터는 그냥 am pm의 구분도 없고 해서 그냥 12를 넘으면 (1~12리스트안에 없으면) 12를 깎는걸로 해결했다.

    print(f'#{test_case} {t} {m}')