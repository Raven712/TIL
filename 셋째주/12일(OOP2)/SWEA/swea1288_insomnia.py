#import sys
#sys.stdin = open("input.txt", "r")

#민석이가 양을 N번 센다. N번 세고나서 나온 숫자를 한글자 한글자씩 기록한다. 기록한 값이 0~9가 다 적히지 않으면 N에 N을 더해서 또 그만큼 양을 센다.
#반복을 해서, 기록한 값이 0~9가 다 적히면, 그때 양을 얼마나 셌을지 계산하는 문제다...

#len(d)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    d = set()
    a = str(N)
    S = N
    count = 1
    for i in a:
        d.add(i)
    while len(d) != 10:
        count += 1
        N = N + S             ### N을 자꾸 N = N * 2로 계산해버려서 한참동안 헤맸다.....
        a = str(N)
        for i in a:
            d.add(i)
        
    print(f'#{test_case} {N}')    