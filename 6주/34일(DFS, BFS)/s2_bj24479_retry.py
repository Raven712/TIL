# 정점 N, 간선 M인 무방향 그래프가 주어짐. 가중치  = 1 
# dfs의 시작은 1부터
# 5 <= N <= 100000
# 1 <= M <= 200000
# 1 <= R <= N

import sys
# sys.stdin = open('dfs.txt', 'r')

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점, 간선, 시작정점 

graph = [[] * m for i in range(n + 1)]
# print(graph)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

for i in range(1, n + 1):
    graph[i].sort()
    # graph[i] = list(reversed(graph[i]))     #이게 맞는걸까?
# print(graph)
visited = [False] * (n + 1)     

cnt = 0
dic_ = {}
# def dfs(start):
#     stack = [start]
#     visited[start] = True
#     global cnt
#     cnt += 1
#     if start not in dic_:
#         dic_[start] = 1
    
#     # while stack:
#     #     cur = stack.pop()           # stack.pop()을 정렬된 리스트에 하면 뒷번호부터 뽑히는데.. 그럼 리스트(그래프)를 뒤로 정렬??
#     #     if not visited[cur]:
#     #         visited[cur] = True
#     #         cnt += 1
#     #         if adj not in dic_:
#     #             dic_[adj] = cnt

#     #     for adj in graph[cur]:          #뒤집으니까 순회할때 adj가 제일 높은수부터 순회를 해버림....
#     #         # if not visited[adj]:        
#     #         #     visited[adj] = True
#     #             stack.append(adj)           # 지금 이 코드는 2 -> 1 까진 괜찮은데, 여기서 1번정점으로 가서 탐색을 하는게아니고 2번정점에서 전부다 탐색을해버림.....
#     #             # cnt += 1
#     #             # if adj not in dic_:
#     #             #     dic_[adj] = cnt
def dfs(start):
    visited[start] = True
    global cnt
    cnt += 1
    if start not in dic_:
        dic_[start] = cnt
    for adj in graph[start] :
        if not visited[adj]:
            dfs(adj)   

dfs(r)
# print(graph)
# print(dic_)

for i in range(1, n + 1):
    if i in dic_:
        print(dic_[i])
    else:
        print(0)