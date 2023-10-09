N, M = map(int, input().split())
bag = []
for y in range(N):
    bag.append(0)

for t in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        bag[x] = k

for r in bag:
    print(r, end = ' ')


