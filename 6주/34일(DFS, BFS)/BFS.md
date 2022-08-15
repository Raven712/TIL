# BFS

- 루트노드에서 인접한노드를 먼저 탐색하는 방법 <-> DFS는 그냥 깊은곳우선으로 들어감



- 두 노드사이의 최단경로를 찾을떄 쓴다. ex) 친구탐색 : dfs하면 모든 친구들을 다봐야할수도있음
  - bfs는 본인 근처사람들부터 탐색해서 금방



- BFS는 재귀적이지 않다.
- 어떤노드를 방문했는지 반드시 체크해야한다. (무한루프가능성)

- 큐 (선입선출)

```python
유방향 그래프를 탐색할떄
from collections import deque

graph = [[] * m for i in range(n + 1)]
for i in range(1, n + 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

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
                
 # 이게 오히려 내가 알던 유사 dfs와 더 닮은것 같다..

```

