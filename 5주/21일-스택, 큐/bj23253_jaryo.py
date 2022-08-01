N, M = map(int,input().split())
I = 0
list_i = []
for i in range(1, (M * 2) + 1):
    ki = list(map(int, input().split()))
    if i % 2 == 0:
        list_i.append(ki)
# list_i = [[a,b] , [c,d], ..[m,n,...,]]
for i in list_i:
    i[-1]                                                       ## 너무어려워서 포기