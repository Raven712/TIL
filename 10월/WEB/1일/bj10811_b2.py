N, M = map(int, input().split())
bag = []
for i in range(1, N + 1):
    bag.append(i)

for x in range(1, M + 1):
    i, j = map(int, input().split())
    temp = bag[i - 1 : j]
    temp = temp[::-1]
    bag[i - 1 : j] = temp

for i in bag:
    print(i, end = ' ')