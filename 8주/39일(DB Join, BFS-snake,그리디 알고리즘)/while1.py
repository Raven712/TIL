# 연산이 두개있음. 1 빼기, 입력된 수로 나누기. 근데 두번째건 정수로 나눠떨어져야 시행가능함. 1이 되기위한 최소연산횟수 출력하기.


n, k = map(int, input().split()) #n이 1되어야하고, k는 나누는 수임.

cnt = 0
while n != 1:
    if n / k == int(n / k):
        n = n / k
        cnt += 1
    else:
        n = n - 1
        cnt += 1

print(cnt)
