# DFS

- 스택 자료구조 (재귀함수) 사용. 방법은 대충 알던대로..



```python
def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if visited[adj] == True:
                continue
            else:
                visited[adj] == True
                stack.append[adj] 
                
## 기존

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

