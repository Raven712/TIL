N = int(input())
for i in range(1, N + 1):
    if i % 2 != 0:
        i = '* ' * N    # N대신 i를 쓰면 별이 계속 늘어나고, N개만큼 찍히는게 맞다.
        print(i)
    else:
        i = ' *' * N
        print(i)
    