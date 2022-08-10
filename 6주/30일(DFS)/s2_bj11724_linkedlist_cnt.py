#N , M은 정점, 간선 개수. uv들이 주어짐. 인접리스트 만들어보자
#정점들을 세트에 등록하고 dfs를 하면서 방문했다면 세트에서 빼자. dfs가 끝났는데도 세트가 비어있지 않다면 cnt를 1 증가시키자. 세트가 빌떄까지 반복하자.
# 간선 없이 정점만 있는경우에도 연결요소는 1이 증가해야한다
import sys
sys.stdin = open('link.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([])

# set_vertex = set()
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    # set_vertex.add(u)
    # set_vertex.add(v)

# list_vertex = list(set_vertex)
visited = [False] * (N + 1)
cnt = 0

def dfs(start):
    stack = [start]
    visited[start] = True
    global cnt
    # list_vertex.remove(start)
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                # list_vertex.remove(adj)
    
    cnt += 1

for i in range(1, N + 1):
    if visited[i] == False:
        dfs(i)
    

print(cnt)
#단순히 cnt2를 증가시키면서 지우면 위에서 set_vertex에 없는 데이터를 지우라는 상황이 발생 --> 오류 / for문으로 해도 set_vertex를 돌면서 요소들을 dfs함수 인자로 넣으면 에러..
# while list_vertex:

# while list_vertex:
#     dfs(list_vertex[0])     ## << 세트는 인덱스지정이 안되지만 리스트는 되니까 리스트로 했음 !! 

# if M == 0:
#     print(N)
# else:
#     print(cnt)
