#로봇이 정사각형영역 S를 이동시킴. 처음에 로봇은 0,0 에 있음. 동쪽보고있음.
#명령들이 다양하게 있고 수행후 로봇이 좌표안에 있어야함. 명령어 여러번하고 그게 !모두! 유효하면 그게 진짜 유효한것

#Turn 0 : 좌측90도회전, Turn  1: 우측 90도회전. Move d : 보는방향으로 d만큼이동.
# 최종위치 출력하기.
# import sys
# sys.stdin = open('robot.txt', 'r')

# M, n = map(int, input().split()) # M은 그래프크기, n은 명령어 개수.

# graph = [ [0] * M for i in range(M) ]               # Turn을 어떻게 표현해야할까? ??
# print(graph)
# robot = [M - 1, 0]      # 그래프와 좌표평면은 180도 회전된거라서?
# cmd_list = []
# cmd2_list = []
# for i in range(n):
#     cmd, cmd2 = input().split()
#     cmd2 = int(cmd2)
#     cmd_list.append(cmd)
#     cmd2_list.append(cmd2)

# turn_l = 0
# turn_r = 0
# dir_ = ['east', 'north', 'west', 'south']
# dic_dir = {'east' : 0, 'north' : 1, 'west' : 2, 'south' : 3}
# dir_status = 'a'
# error = 0
# for i in range(1, n):
#     if not i - 1 and cmd_list[i - 1] == 'MOVE':
#         dir_status = 'east'
#         robot[1] += cmd2
#         continue
#     if cmd_list[i - 1] == 'TURN' and cmd2_list[i - 1] == 0:
#         turn_l += 1
#     elif cmd_list[i - 1] == 'TURN' and cmd2_list[i - 1] == 1:
#         turn_r += 1
#     if cmd_list[i] == 'MOVE':
#         s = (turn_l - turn_r) % 4
#         dir_status = dir_[(dic_dir[dir_status] + s) % 4]
#         # print(dir_status)
#         turn_l = 0
#         turn_r = 0
#         if dir_status == 'east':
#             robot[1] += cmd2_list[i]
#         elif dir_status == 'north':
#             robot[0] += cmd2_list[i]
#         elif dir_status == 'west':
#             robot[1] -= cmd2_list[i]
#         elif dir_status == 'south':
#             robot[0] -= cmd2_list[i]
#     if robot[0] < 0 or robot[1] < 0:
#         print(-1)
#         error += 1
#         break
# if not error:
#     print(robot)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import sys
sys.stdin = open('robot.txt', 'r')

M, n = map(int, input().split()) # M은 그래프크기, n은 명령어 개수.

# graph = [ [0] * M for i in range(M) ]               # Turn을 어떻게 표현해야할까? ??

robot_y = M  #0, 0 을 그래프에서 본 좌표
robot_x = 0
dy = [0, -1, 0, 1] #동 북 서 남 (90도 회전순서)
dx = [1, 0, -1, 0]
# stack_dir = ['east']
# dic_ = {'east' : (dy[0], dx[0]), 'north' : (dy[1], dx[1]), 'west' : (dy[2], dx[2]), 'south' : (dy[3], dx[3])}
dir_cur = (0, 1)
dic_0  = {(0, 1) : (-1, 0), (-1, 0) : (0, -1), (0, -1) : (1, 0), (1, 0) : (0, 1)}
dic_1 = {(0, 1) : (1, 0), (1, 0) : (0, -1), (0, -1) : (-1, 0), (-1, 0) : (0, 1)}

cancel = 0 # 좌표가 범위밖으로 나갔을때 프로그램을 종료시킬 변수
for i in range(n):
    cmd, cmd2 = input().split() # Move 10 이런것
    if cmd == 'MOVE':
        robot_y += dir_cur[0] * int(cmd2)
        robot_x += dir_cur[1] * int(cmd2)
        if 0 > robot_y or robot_y > M or 0 > robot_x or robot_x > M: # 좌표가 둘중하나라도 이동 후 범위밖으로 나가면 종료
            print(-1)
            cancel += 1
            break
    elif cmd == 'TURN' and cmd2 == '0':
        dir_cur = dic_0[dir_cur]
    elif cmd == 'TURN' and cmd2 == '1':
        dir_cur = dic_1[dir_cur]


if not cancel:
    print(robot_x, M - robot_y)        # 좌표평면과 그래프의 좌표는 다르다..
        

        

