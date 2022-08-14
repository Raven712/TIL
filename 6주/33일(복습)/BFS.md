# BFS

- 그래프에서 기준노드중심으로 가까운노드부터 우선적으로 탐색. (최단거리 탐색!!! - 미로찾기)
  - 시작노드를 큐에 넣고 방문처리.
  - 큐에서 노드를 꺼낸뒤 해당노드의 인접노드중 방문하지않은 노드를 모두 큐에 삽입하고 방문처리
  - 반복불가까지 반복



``` python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```



문제

```python
그냥 섬의개수 찾기같은 문제


```

