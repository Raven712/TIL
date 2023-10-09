N = int(input())
list_ = list(map(int,input().split()))
con = int(input())
ans = 0
for i in list_:
    if i == con:
        ans += 1
print(ans)