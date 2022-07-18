a, m, d, n = map(int,input().split())

b = (a * m) + d 
for i in range(1, n-1):
    i = b
    b = (i * m) + d
if  n == 1:
    print(a)
else:
    print(b)