#전형적인 DFS 문제
import sys
sys.stdin = open('virus.txt', 'r')

n = int(input()) #컴퓨터 개수

m = int(input()) #네트워크상에 직접연결된 컴퓨터쌍의 수 (간선의 수인듯.)

graph = [ [] * m for i in range(n + 1)]
visited = [False] * (n + 1)

cnt = 0
def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        global cnt
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                cnt += 1

# print(graph)
# print(visited)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)


dfs(1)
print(cnt)
        
