# 정점 N, 간선 M인 무방향 그래프가 주어짐. 가중치  = 1 
# dfs의 시작은 1부터
# 5 <= N <= 100000
# 1 <= M <= 200000
# 1 <= R <= N
import sys
sys.stdin = open('dfs.txt', 'r')

n, m, r = map(int, input().split()) # 정점, 간선, 시작정점 

graph = [[] * m for i in range(n + 1)]
# print(graph)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n + 1):  
    graph[i].sort()
    graph[i] = graph[i][::-1]
# print(graph)

visited = [False] * (n + 1)
dic_ = {}
cnt = 0
def dfs(start):
    stack = [start]
    visited[start] = True
    global cnt
    while stack:
        cur = stack.pop()
        cnt += 1
        if cur not in dic_:
            dic_[cur] = cnt

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)           
dfs(r)
print(graph)
for i in range(1, n + 1):
    if i in dic_:
        print(dic_[i])
    else:
        print(0)
