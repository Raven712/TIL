N, M = map(int, input().split())
bag = []

for i in range(1, N + 1):
    bag.append(i)

for k in range(M):
    i, j = map(int, input().split())
    i_ = bag[i - 1]
    j_ = bag[j - 1]
    bag[i - 1] = j_
    bag[j - 1] = i_

for i in bag:
    print(i, end = ' ')

