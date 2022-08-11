
import sys
sys.stdin = open('chonsu.txt', 'r')

n = int(input()) # 정점의 개수 (사람수)
c1, c2 = map(int, input().split())

graph = []
for i in range(n + 1):
    graph.append([0] * (n + 1))

# graph = [[] for i in range(n + 1)]
m = int(input())
for i in range(m):
    x, y = map(int, input().split())  #x, y는 부모자식관계
    graph[x].append(y)  #무방향 인접그래프생성
    graph[y].append(x)

visited = [False] * (n + 1)
#촌수계산을 하려면 stack에 촌수도 넣어줌 

def dfs(start):
    start = 7
    visited[start] = True
    stack = [start, 0]
    cur, count = stack.pop()
    print(cur, count)
    while stack:
        cur, count = stack.pop()
        if cur == end:
            answer = count
            break

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj, count + 1)
    return answer

a= dfs(7)
print(a)