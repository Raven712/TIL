import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b ,c ,d ,e, f, g, h, i, j = map(int,input().split())
    mean = (a+b+c+d+e+f+g+h+i+j) / 10
    print('#', end ='')
    print(test_case, end = ' ')
    print(math.floor(round(mean, 0)
    ))