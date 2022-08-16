# n개 정점, m개 간선, 무방향 그래프. 가중치 1. 정점 r에서 시작해서 bfs 탐색으로 노드방문할떄, 방문순서는? -> 오름차순으로 출력.
import sys
# sys.stdin = open('bfs.txt', 'r')
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] * m for i in range(n + 1)]

for i in range(m):
    u, v  = map(int, input().split()) #간선의 정보
    graph[u].append(v)
    graph[v].append(u) #무방향(양방향)

# print(graph)
# [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

for i in range(1, n + 1):
    graph[i].sort()         #bfs를 할때, queue.popleft() 를 하기때문에 정렬이 되어있어야 오름차순으로 방문을 한다. (bfs자체가 원래 이런듯?)

visited = [False] * (n + 1)

cnt = 0 # 순서를 기록할 변수
queue = deque()
dic_ = {}   # cnt(방문한 순서)와 현재 정점을 매칭시키려고 만듬. 
def bfs(start):
    visited[start] = True
    queue.append(start)
    global cnt
    cnt += 1
    if start not in dic_:
        dic_[start] = cnt
    while queue:
        cur = queue.popleft()   #큐의 제일왼쪽(먼저들어온거)을 꺼냄.
        
        for adj in graph[cur]:  # 그래프의 cur번 정점에 연결된 모든 다른정점들을 순회한다. 다른정점들이 거리가 같기때문에 전부다 순회해주는것.
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)   #순회하는걸 방문표시하면서, 큐에 넣어준다.
                cnt += 1
                dic_[adj] = cnt     #adj가 dic_에 있는지 없는지 굳이 확인하지않아도 된다( 어차피 if not visited[adj]가 똑같은 거름망역할을 해서 )

bfs(r)
# print(dic_)
# {1: 1, 2: 2, 4: 3, 3: 4}  정상적으로 방문된걸 알수있음.

for i in range(1, n + 1):
    if i not in dic_:
        print(0)
    else:
        print(dic_[i])
