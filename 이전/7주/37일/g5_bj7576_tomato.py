# n x m 행렬이 있다 (창고). 보관후 하루지나면 익은토마토 근처의 익지않은 토마토가 익게된다. 인접은 사방이다.토마토가 다 익으려면 최소 며칠이 필요한가?
# 1은 익은 토마토, 0은 안익은 토마토, -1은 토마토가 안들어있음. 만약, 모두 익는 상황이 안나오면 -1을 출력해야함. 저장될때부터 다 익었다면 0출력해야댐.
import sys
sys.stdin = open('tomato.txt', 'r')
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split()) # 2~ 1000.

graph = [list(map(int, input().split())) for i in range(n)]
# print(graph)

dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]
dic_tomato = {}
# cnt = 0 # 모든좌표를 탐색하면서, 1의 개수(토마토개수) 가 좌표전체개수와 같다면 (모든곳에 이미 토마토가 심어져있다면) 을 하려고 했으나 이미 정상적인 bfs라면 알아서 걸러주는듯?? (그냥 0일차에서 끝)
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            dic_tomato[(y, x)] = (y, x)

queue = deque()

for i in dic_tomato:
    for d in range(4):
        ny = i[0] + dy[d]
        nx = i[1] + dx[d]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
            graph[ny][nx] = graph[i[0]][i[1]] + 1
            queue.append((ny, nx))
# print(queue)
while queue:
    r, c = queue.popleft()
    for d in range(4):
        nr = r + dy[d]
        nc = c + dx[d]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
            graph[nr][nc] = graph[r][c] + 1
            queue.append((nr, nc))
# print(graph)
# [[9, 8, 7, 6, 5, 4], [8, 7, 6, 5, 4, 3], [7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 1]]
# print(queue)
cancel = 0
date = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:        # 이미 토마토가 익는과정을 거쳤는데, 0이 존재한다면 못익은 토마토가 존재한 상황이다.
            print(-1)
            cancel = 1
            break
        else:
            if graph[i][j] >= date:     #이중그래프의 최대치를 출력하기위해 위의 과정(0이 남아있는지 여부)을 거치면서 동시에 최대값도 입력해줬다. 그래프의 요소에 적힌 값은 결국 날짜다. 
                date = graph[i][j]
    if cancel == 1:
        break
if cancel == 1:
    pass
else:
    print(date - 1)     # 첫날이 1일이므로, 마지막 결과에서 1을 빼준다.
