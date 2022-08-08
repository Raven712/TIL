N, k =map(int,input().split())

x = list(map(int,input().split())) #길이 N

x= sorted(x)[::-1]

print(x[k-1])

