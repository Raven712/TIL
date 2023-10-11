T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    ans = []
    for i in S:
        ans.append(R * i)
    for i in ans:
        print(i, end = '')
    print('')
    