#1로 연결된것 (DFS) . 가로세로만 연결되어있어야하고, 대각선만 연결된건 다른그림임. 그림들중 가장 넓은 넓이 , 그림의 개수 출력
import sys
sys.stdin = open('painting.txt', 'r')

n, m = map(int, input().split())    #n x m 행렬

grim = []
for i in range(n):
    grim.append(list(map(int, input().split())))

# print(grim)
painting_size = []

visited = [[False] * m for i in range(n)]
# print(visited)
dy = [-1, 1, 0, 0] #상 하 좌 우
dx = [0, 0, -1, 1]


def dfs(y, x, painting_size):
    visited[y][x] = True
    painting_size += 1

# for y in range(n):
#     for x in range(m):
#         if visited[y][x] == True:
#             continue
#         dic_graph[(y, x)] = []
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if 0 <= ny < n and 0 <= nx < m:
#                 visited.append((ny, nx))
#                 dic_graph[(y, x)] += [(ny, nx)]

# def dfs(start : tuple):
#     stack = [start]
#     visited.append(start)
#     while stack:
#         cur = stack.pop()
#         for adj in dic_[cur]:
#             if adj not in visited:
#                 visited.append(adj)
#                 stack.append(adj)