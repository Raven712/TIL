import sys
sys.stdin = open('ㅇ.txt', 'r')
# 19x19가 판임. 1은 검정 2는 흰 0은 빈곳
board = [list(map(int, input().split())) for i in range(19)]

dx = [-1,0,1,-1,1,-1,0,1]   #좌측상단 -> 우측상단, .. 좌측하단 -> 우측하단.
dy = [1,1,1,0,0,-1,-1,-1]
dx2 = [-2,0,2,-2,2,-2,0,2]
dy2 = [2,2,2,0,0,-2,-2,-2]
dx3 = [-3,0,3,-3,3,-3,0,3]
dy3 = [3,3,3,0,0,-3,-3,-3]
dx4 = [-4,0,4,-4,4,-4,0,4]
dy4 = [4,4,4,0,0,-4,-4,-4]
dx5 = [-5,0,5,-5,5,-5,0,5]      # 6연속도 확인해야함. 6연속 같은색이면 승리가아님. 범위설정은?? 밑에서 i, j가 5이상일때만 6연속으로 같은색인지 고려함.
dy5 = [5,5,5,0,0,-5,-5,-5]

# for i in range(4):
#     for j in range(4):
        

nx1 = 0
ny1 = 0
nx2 = 0
ny2 = 0
nx3 = 0
ny3 = 0
nx4 = 0 
ny4 = 0
nx5 = 0
ny5 = 0    
stop = True
for i in range(19):
    for j in range(19):
        if board[i][j] == 1:
            for k in range(8):
                nx1 = i + dx[k]
                ny1 = j + dy[k]
                nx2 = i + dx2[k]
                ny2 = j + dy2[k]
                nx3 = i + dx3[k]
                ny3 = j + dy3[k]
                nx4 = i + dx4[k]
                ny4 = j + dy4[k]
                nx5 = i + dx5[k]
                ny5 = j + dy5[k]
        
                if 0 <= nx1 < 19 and 0 <= ny1 < 19 and 0 <= nx2 < 19 and 0 <= ny2 < 19 and 0 <= nx3 < 19 and 0 <= ny3 < 19 and 0 <= nx4 < 19 and 0 <= ny4 < 19 and 0 <= nx5 < 19 and 0 <= ny5 < 19:
                    if board[nx1][ny1] == 1 and board[nx2][ny2] == 1 and board[nx3][ny3] == 1 and board[nx4][ny4] == 1 and board[nx5][ny5] != 1:
                        print(1)
                        list_x = [i, nx1, nx2, nx3, nx4]
                        list_y = [j, ny1, ny2, ny3, ny4]
                        print(min(list_x) + 1, min(list_y) + 1)  # 좌표중에 제일 원점과 가까운 좌표를 출력하는데, 좌표는 1부터 시작이라 1을 더해줌.
                        stop = False
                        break
                elif i < 5
        if stop == False:
            break
    if stop == False:
        break                # if board[i + dx[k]][j + dy[k]] == 1 and board[i + dx2[k]][j+ dy2[k]] == 1 and board[i + dx3[k]][j+ dy3[k]] == 1 and board[i + dx4[k]][j+ dy4[k]] == 1 and board[i + dx5[k]][j+ dy5[k]] != 1:
                    #     print(1)
                    #     list_x = [i + dx[k], i + dx2[k], i + dx3[k], i + dx4[k]]
                    #     list_y = [j + dy[k], j + dy2[k], j + dy3[k], j + dy4[k]]
                    #     print(min(list_x) + 1, min(list_y) + 1) # 좌표중에 제일 원점과 가까운 좌표를 출력하는데, 좌표는 1부터 시작이라 1을 더해줌.

                # elif i == 4 and j ==4:
                #     if board[i + dx[k]][j + dy[k]] == 1 and board[i + dx2[k]][j+ dy2[k]] == 1 and board[i + dx3[k]][j+ dy3[k]] == 1 and board[i + dx4[k]][j+ dy4[k]] == 1:
                #         print(1)
                #         ist_x = [i + dx[k], i + dx2[k], i + dx3[k], i + dx4[k]]
                #         list_y = [j + dy[k], j + dy2[k], j + dy3[k], j + dy4[k]]
                #         print(min(list_x) + 1, min(list_y) + 1)
                # elif i ==5 and j ==4:
                #     if board[i + dx[k]][j + dy[k]] == 1 and board[i + dx2[k]][j+ dy2[k]] == 1 and board[i + dx3[k]][j+ dy3[k]] == 1 and board[i + dx4[k]][j+ dy4[k]] == 1 and board[i +dx5[k]]
                #         print(1)
                #         ist_x = [i + dx[k], i + dx2[k], i + dx3[k], i + dx4[k]]
                #         list_y = [j + dy[k], j + dy2[k], j + dy3[k], j + dy4[k]]
                #         print(min(list_x) + 1, min(list_y) + 1)

# 같은내용을 흰돌에도 적용시킴.

for i in range(19):
    for j in range(19):
        if board[i][j] == 2:
            for k in range(8):
                nx1 = i + dx[k]
                ny1 = j + dy[k]
                nx2 = i + dx2[k]
                ny2 = j + dy2[k]
                nx3 = i + dx3[k]
                ny3 = j + dy3[k]
                nx4 = i + dx4[k]
                ny4 = j + dy4[k]
                nx5 = i + dx5[k]
                ny5 = j + dy5[k]
                if 0 <= nx1 < 19 and 0 <= ny1 < 19 and 0 <= nx2 < 19 and 0 <= ny2 < 19 and 0 <= nx3 < 19 and 0 <= ny3 < 19 and 0 <= nx4 < 19 and 0 <= ny4 < 19 and 0 <= nx5 < 19 and 0 <= ny5 < 19:
                    if board[nx1][ny1] == 2 and board[nx2][ny2] == 2 and board[nx3][ny3] == 2 and board[nx4][ny4] == 2 and board[nx5][ny5] != 2:
                        print(2)
                        list_x = [i, nx1, nx2, nx3, nx4]
                        list_y = [j, ny1, ny2, ny3, ny4]
                        print(min(list_x) + 1, min(list_y) + 1) 
                        



# for i in range(4, 19):
#     for j in range(4, 19):
#         if board[i][j] == 2:
#             for k in range(8):
#                 if i and j >=5:
#                     if board[i + dx[k]][j + dy[k]] == 2 and board[i + dx2[k]][j+ dy2[k]] == 2 and board[i + dx3[k]][j+ dy3[k]] == 2 and board[i + dx4[k]][j+ dy4[k]] == 2 and board[i + dx5[k]][j+ dy5[k]] != 2:
#                         print(2)
#                         list_x = [i + dx[k], i + dx2[k], i + dx3[k], i + dx4[k]]
#                         list_y = [j + dy[k], j + dy2[k], j + dy3[k], j + dy4[k]]
#                         print(min(list_x) + 1, min(list_y) + 1) 
#                 else:
#                     if board[i + dx[k]][j + dy[k]] == 2 and board[i + dx2[k]][j+ dy2[k]] == 2 and board[i + dx3[k]][j+ dy3[k]] == 2 and board[i + dx4[k]][j+ dy4[k]] == 2:
#                         print(2)
#                         ist_x = [i + dx[k], i + dx2[k], i + dx3[k], i + dx4[k]]
#                         list_y = [j + dy[k], j + dy2[k], j + dy3[k], j + dy4[k]]
#                         print(min(list_x) + 1, min(list_y) + 1)
                