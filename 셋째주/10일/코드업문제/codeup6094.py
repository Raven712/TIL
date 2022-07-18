n = int(input())
k = input().split()
for i in range(n):
    k[i] = int(k[i])
min = k[0]
for i in range(n):
    if k[i] < min:
        min = k[i]
print(min)
