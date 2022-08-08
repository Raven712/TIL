t = int(input())
for i in range(t):
    s = int(input()) #값
    n = int(input())    #옵
    price = s
    for j in range(n): 
        q, p = map(int, input().split())
        #q = 옵션수 p는 가격
        price += q * p
        
    print(price)