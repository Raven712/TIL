# 미로탐색은 대표적인 bfs문제라고 한다. dfs로는 풀수없나?

# 이 문제는 이전에 했던것처럼 단순히 cnt 를 늘려가면서는 풀수없다. bfs를 할떄, 한 정점에서 인접정점을 방문했을때 혹은 그 정점에서의 bfs가 끝났을때 cnt를 증가시키는 방법을 하면,
# 예를들어 맨구석자리의 벽에 맞닿았을때도 cnt가 증가해서 틀린답이 나온다.
# 그래서 한 정점에서 인접정점으로 이동한 정점을 + 1 시켜주는것으로 풀어야한다.

import sys
# sys.stdin = open('labyrinth.txt', 'r')
input = sys.stdin.readline
from collections import deque

# n x m 행렬이 주어짐. 미로를 탈출하기위해 (1,1에서 N,M으로 가야함) 어떻게 해야할까.

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for i in range(n)]
# print(graph)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1] #상 하 좌 우

cnt = 0
queue = deque()
queue.append((0, 0))
# for y in range(n):
#     for x in range(m):
#         if graph[y][x] == 0:
#             continue
#         graph[y][x] = 0 #방문.
#         queue.append((y, x))
while queue:
    r, c = queue.popleft()
    for d in range(4):
        ny = r + dy[d]
        nx = c + dx[d]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
            graph[ny][nx] = graph[r][c] + 1 #방문
            queue.append((ny, nx))
    
            
print(graph[n-1][m-1])