# dfs, bfs를 구현하는 문제. n은 정점개수, m은 간선 개수. 탐색 시작하는 번호 v.

import sys
sys.stdin = open('dfsbfs.txt', 'r')
sys.setrecursionlimit(10 ** 6)
from collections import deque

n, m, v = map(int, input().split())

graph = [[] * m for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split()) #정점끼리 연결된 간선?
    graph[a].append(b)
    graph[b].append(a)
# print(graph)                # dfs, bfs하기위해서는, 그래프를 정렬해야하는것 같다 !!

for i in range(1, n + 1):           #확실히 이게맞다!!!!!!!!!!!!!!!!!!!
    graph[i].sort()

visited = [False] * (n + 1)

def dfs(start):
    visited[start] = True
    print(start, end = ' ')
    for adj in graph[start]:
        if not visited[adj]:
            # visited[adj] = True    <<< 어차피 다음 dfs에서 알아서 True로 바꿔준다.
            dfs(adj)
dfs(v)
print()

visited = [False] * (n + 1)
def bfs(start):
    visited[start] = True
    queue = deque([start])  # [v] 에서, popleft를 한다.. 즉 처음의 cur == v다. 
    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)
bfs(v)
