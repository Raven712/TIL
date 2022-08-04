#체스말. 킹1 퀸1 룩2 비숍2 나이트2 폰8
#몇개빼거나 더해야 정상되나

# 0 -> 1
# 2 -> -1

list_ = list(map(int,input().split()))
# dic_chess = {
#     'king' : 1,
#     'queen' : 1,
#     'luke' : 2
#     'bishop' : 2
#     'knight' : 2
#     'pawn' :8
# }

list_chess = [1,1,2,2,2,8]

for i in range(6):
    list_[i] = -1 * (list_[i] - list_chess[i])

for i in list_:
    print(i, end = ' ')
