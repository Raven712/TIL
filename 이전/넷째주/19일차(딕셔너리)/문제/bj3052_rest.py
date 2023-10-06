ans2 = set()
for i in range(10):
    A = int(input())
    ans = A % 42 
    ans2.add(ans)
print(len(ans2))