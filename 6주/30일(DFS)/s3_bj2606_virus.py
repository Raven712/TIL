import sys
sys.stdin = open('virus.txt', 'r')

#인접리스트가 입력으로 주어진다

# N = int(input())
# M = int(input())

# graph = []
# visited = []
# for i in range(N):
#     graph.append([0] * N)
#     visited.append(False)



# def dfs(start):
#     stack = [start]
#     visited[start] = True
#     while len(stack) != 0:
#         cur = stack.pop()

#         for adj in graph[cur]:
#             if not visited[adj]:
#                 stack.append(adj)

n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
total = 0

#인접 리스트
for i in range(m):
    v1, v2 = map(int, input().split())
	graph[v1].append(v2)
    graph[v2].append(v1)
    

def dfs(start):
    stack = [start]
    visited[start] = True
    
    while stack:
        cur = stack.pop()
        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

dfs(1)

print(visited)