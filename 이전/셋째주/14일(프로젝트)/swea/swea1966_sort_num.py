#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    print(f'#{test_case}', end = ' ')
    b = 0
    for i in range(len(a)):      # range로 하지않고 리스트 a를 그자체로 순회하면, i가 a의 마지막 요소임을 표현하기가 힘들어짐 ( i == a[:-1] 을 해도, 같은 값이 반복될시 줄바꾸기가 여러번됨)
        b = a[i]             # b를 쓰지않고 i를 쓰면, 아래 줄바꾸기에서 오류가난다 !! (i가 이미 a[i]로 할당돼버려서)
        print(b, end = ' ')
        if i == len(a) - 1:         
            print('')

    #