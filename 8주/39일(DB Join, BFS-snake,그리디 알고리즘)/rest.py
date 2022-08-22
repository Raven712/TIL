# 거스름돈이 500 100 50 10원 있음. N원 거슬러줘야할때 동전을 최소 몇개 줘야할까?

n = int(input())

cnt = 0
while n:
    if n >= 500:
        n = n - 500
        cnt += 1
    elif 500 > n >= 100:
        n = n - 100
        cnt += 1
    elif 100 > n >= 50:
        n = n - 50
        cnt += 1
    elif 50 > n >= 10:
        n = n - 10
        cnt += 1


print(cnt)