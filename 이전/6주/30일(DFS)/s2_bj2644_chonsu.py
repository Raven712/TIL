# 인접 리스트가 주어짐. #c1과 c2간의 촌수가 몇촌관계인지 계산하기 -- > c1에서 c2까지의 거리.. 이건 인접행렬로 풀어야하지않을까 ? -- > 아닌것같다....
import sys
sys.stdin = open('chonsu.txt', 'r')
from pprint import pprint

n = int(input()) # 정점의 개수 (사람수)
c1, c2 = map(int, input().split())

graph = []
for i in range(n + 1):
    graph.append([0] * (n + 1))

m = int(input()) # 간선의 개수 (관계의 수)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n + 1)
def dfs(start):
    stack = [start]
    visited[start] = True

    current = stack.pop()
    for adj in graph[current]:
        if visited[adj] == False:
            visited[adj] = True
            stack.append(adj)

pprint(graph)