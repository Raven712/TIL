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
가장 간단한 dfs

import sys
sys.setrecursionlimit(10 ** 6)

visited = [False] * n
def DFS(start) :
    visited[start] = True
    for adj in graph[start] :
        if not visited[adj]:
            DFS(adj)    
```





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

                
#위의코드는 틀렸음. 저렇게하면 dfs가 아니게됨(for adj in graph[cur])

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        if not visited[cur]:		#pop해주고 난다음에 바로 방문처리를 해준다.
            visited[cur] = True
            
        for adj in graph[cur]:
            if not visited[adj]:
                stack.append(adj)
                
# 혹은 queue를 이용해서 popleft를 써야함.맨위의코드와 동일하게 하고, stack 대신 queue를 사용.
#근데 이건 그냥 bfs임. (dfs 아님)

queue = deque()

def bfs(start):
    visited[start] = True                # 시작 정점 방문 처리
    queue.append(start)                    # 돌아갈 곳 기록

    while queue:                        # 덱이 빌 때까지(돌아갈 곳이 없을 때까지) 반복
        cur = queue.popleft()            # 현재 방문 정점(후입선출)

        for adj in graph[cur]:            # 인접한 모든 정점에 대해
            if not visited[adj]:        # 아직 방문하지 않았다면
                visited[adj] = True        # 방문처리
                queue.append(adj)        # 덱에 넣기
                print(visited
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



## 추가

DFS 는 백트래킹을 한다.

--> 첫번째 정점의 간선중 첫번째 고름 -> 간선을 통해서 간 정점에서 또 첫번쨰 고름 ->...

--> 못가면, 그 전 탐색지로 돌아와서, 안간곳이 있는지 탐색함. 이런식이다 !!!!!!!
