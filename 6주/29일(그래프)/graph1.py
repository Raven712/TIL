# 무방향 그래프 표현하기.

N, M = map(int, input().split())
# graph = [[0] * (N + 1)] * (N + 1) # 이렇게하니까 안의 모든리스트들이 하나의 데이터주소를 가진다
graph = []
for i in range(N + 1):
    graph.append([0]* (N+1))
for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
print(graph)            #인접 행렬 출력

list_adj = [[] * (N + 1) for i in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            list_adj[i].append(j)
print(list_adj)

