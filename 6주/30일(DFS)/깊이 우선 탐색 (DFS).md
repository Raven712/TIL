# 깊이 우선 탐색 (DFS)



### 그래프 탐색 알고리즘

- 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘 ..!!! 



- 이 알고리즘엔 깊이우선탐색, 너비우선탐색이 있음.
  - 스택, 큐 자료구조의 개념을 함께 활용함.
    - 스택 + 그래프 == 깊이 우선 탐색(DFS). (그래프의 깊이를 우선으로 탐색하려고 스택개념 활용)
    - 큐 + 그래프 == 너비 우선 탐색(BFS) (그래프의 너비를 우선으로 탐색하기 위해 큐 개념 활용)



- 깊이우선(DFS) : 한쪽끝까지 다 찾아보고 돌아와서 다른곳으로 넘어감..
- 너비우선(BFS) : 특정 깊이에 있는 정점을 전부 탐색하고 다음으로 넘어가는식  (최단거리찾기에 좋음)





### DFS (깊이우선탐색)

- 미로탈출이라고 생각하면된다
  - 어느 길로 가장 깊게갔다가 막히면 돌아와서 다른길을 탐색하는것



- 모든 정점을 다 방문할 때 유리함. ---> ** 경우의 수, 순열-조합에서 사용됨 **
  - 그러므로 모든 정점을 다 볼 필요가 없거나 , 최단거리 탐색시 BFS 가 더 유리하다.



```python
일단 탐색할 그래프 필요
--> 인접행렬 혹은 리스트로 표현가능함.

각 정점을 방문했는지 여부를 판별할 리스트가 필요함.
# N (여기선 7)개의 정점이 있을때

visited = [False, False, False, False, False, False, False]
# visited = [False] * N 
# 방문하게되면 True 로 전환

DFS의 사이클
1. 현재 정점 방문 처리
2. 인접 모든 정점 확인
3. 방문하지 않은 인접 정점 이동

def dfs(start):
    stack = [start] #돌아갈곳 기록
    visited[start] = True #시작정점 방문처리
    while stack: # 스택이 빌 때 까지 (돌아갈곳 없을떄까지) 반복 -> .while len(stack) != 0과같음
        cur = stack.pop() #현재 방문 정점(후입선출, LIFO)
        
        for adj in graph[cur]: #인접 모든 정점에 대해
            if not visited[adj]: # 아직 방문하지않았다면
                visited[adj] = True #방문 처리
                stack.append(adj) #스택에 넣음 

```



```python
# 바이러스 문제

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
    

```

