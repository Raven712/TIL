T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):    ## 접근을 level만 보고 세트, 딕셔너리의 길이로 문제를 풀려고 접근했는데, 다 짜고보니 ooooooo같은건 회문인데 세트길이는 1이라 그냥 무조건 틀린 접근법이었음...
    a = input()
    b = a[::-1]  ## 이게 핵심이었음
    if a == b:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')