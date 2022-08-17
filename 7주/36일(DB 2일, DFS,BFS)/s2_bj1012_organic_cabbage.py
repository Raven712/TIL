# 지렁이는 배추근처서식. 배추근처에 지렁이가 있어야함. --> 상하좌우.
import sys
# sys.stdin = open('organic.txt', 'r')
input = sys.stdin.readline
# from pprint import pprint
from collections import deque


T = int(input()) #T.C

for i in range(T):
    m, n, k = map(int, input().split()) # n x m 행렬이며, k는 정점의 개수임.
    graph = [ [0] * m for j in range(n) ]
    # print(graph)
    for j in range(k):
        x, y = map(int, input().split()) # (y, x) 에 배추가 위치한다.
        graph[y][x] += 1
    # pprint(graph)
    # [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    # [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    dy = [-1, 1, 0, 0] #상 하 좌 우
    dx = [0, 0, -1, 1]

    worm = 0
    queue = deque()
    # def dfs(y, x):
    #     if graph[y][x] == 1:
    #         graph[y][x] = 0 # 방문표시


    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:        #방문했거나 배추가 없다면 다음순회로
                continue
            worm += 1
            queue.append((r, c))
            while queue:
                r2, c2 = queue.popleft()
                for d in range(4):
                    nr = r2 + dy[d]
                    nc = c2 + dx[d]
                    if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                        graph[nr][nc] = 0
                        queue.append((nr, nc))
    print(worm)