N, M = map(int,input().split())

#0 은 공백 1은 붕어. 좌우대칭을 시켜야함

boonger_list = []
for i in range(N):
    boonger = input()
#     boonger_list.append(list(boonger))

# for i in range(N):
#     for j in range(M):
#         boonger_list[i][j] = boonger_list[j][i]

# print(boonger_list)
    print(boonger[::-1])