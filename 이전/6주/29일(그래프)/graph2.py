import sys
sys.stdin = open('d.txt', 'r')

N, M = map(int, input().split())
graph = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
print(graph)

list_adj = [[] * (N + 1) for i in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            list_adj[i].append(j)
print(list_adj)