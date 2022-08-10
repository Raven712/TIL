n = 5

graph = []
for i in range(n + 1):
    graph.append([0] * (n + 1))

m = int(input()) # 간선의 개수 (관계의 수)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    