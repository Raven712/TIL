# A길이 10. 자연수만. 3번째 큰수 출력하기

T = int(input())

for i in range(T):
    A = list(map(int,input().split()))
    count = 0
    while count != 2:
        A.remove(max(A))
        count += 1
    print(max(A))