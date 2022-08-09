# 6목은 안된다. 범위를 만족시켜줘야한다. 검은색 승리1 흰색승리2 승부안난건 0

#델타탐색을 8방향할게아니고 우측으로 해줘야됨 // 가장작은 xy값을 출력해야해서 ( 승리한 바둑알의 좌표중 ) << 가장작은 xy가 아니고 가장 왼쪽의 알 좌표출력해야해서
import sys
sys.stdin = open('ㅇ.txt', 'r')

board = []

for i in range(19):
    board.append(list(map(int,input().split())))

dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1] #우 하 우하 우상

answer = 0

for y in range(19):
    for x in range(19):
        if board[y][x] == 1 or 2:
            for d in range(4):
                next_y = y + dy[d]
                next_x = x + dx[d]
                cnt = 1
                while True: #조건2개. 범위벗어나지않고 같은색이 나와야함
                    #범위
                    if not ( -1 < next_y < 19 and -1 < next_x < 19):
                        break
                    
                    #돌 색
                    if board[next_y][next_x] != board[y][x]:
                        break


                    #다음좌표 탐색
                    next_y = y + dy[d]
                    next_x = x + dx[d]

                    cnt += 1
                    next_y = next_y + dy[d]
                    next_x = next_x + dx[d]
                    if cnt == 5:
                        prev_y = y - dy[d]
                        prev_x = x - dx[d]

                        #기준좌표의 이전좌표가 범위를 벗어날때 + 기준좌표값과 이전좌표값이 다를때 오목이됨. (둘중하나만. 이미 cnt는 5니까)
                        if not (-1 < prev_y < 19 and -1 < prev_x < 19) or board[y][x] != board[prev_y][prev_x]:
                            answer = board[y][x] #누군가 승리했을떄 answer에 0이아닌값을 넣어줌
                            print(board[y][x]) #현재돌의 색 출력
                            print(y + 1, x + 1) #좌표

if answer == 0: #무승부일땐 그냥 아무변수나 넣은 answer가 0인게 유지되면 출력
    print(answer)              
            