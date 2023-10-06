# N x M 행렬이 주어지는데, 첫입력이 N, M이다. 그후로 N개의 입력과 얼음틀이 주어진다. 0은 음료수고 1은 칸막이다. 4방향 탐색을 해서 음료수가 있으면 같은음료수고, 아니라면 아이스크림이 한개 생기는 그런개념.
import sys
sys.stdin = open('freeze.txt', 'r')

N, M = map(int, input().split())
graph = [list(int(input()) for i in range(N))] 

dy = [0, 0, -1, 1] # 동 서 남 북
dx = [1, -1, 0, 0]


visited = [[False] * M for i in range(N)]

for y in range(N):
    for x in range(M):
        if visited[y][x]:   #이미방문했다면 넘어간다.
            continue
        if graph[y][x] == 1:  # 칸막이라면 넘어간다.
            continue
        # stack = [y, x]        
        # visited[y][x] = True    # 여기까지 진행됐다면 오지않은곳이었던곳이니 방문표시를 한다.
        # while stack:
        #     cur = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == True:     #탐색하는곳이 이미 탐색됐으면 스킵
                    continue
                if graph[ny][nx] == 1:          # 탐색하는곳이 칸막이라면 스킵
                    continue
                visited[ny][nx] = True
                





#여기서부터 막힌다. ... dfs부터? 인접리스트생성부터?
"""""""""""""""""""""""""""""""""""""""""""""""""""""


visited = [[False] * M for i in range(N)]

for y in range(N):
    for x in range(M):
        if visited[y][x]:   #이미방문했다면 넘어간다.
            continue
        if graph[y][x] == 1:  # 칸막이라면 넘어간다.
            continue
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == True:     #탐색하는곳이 이미 탐색됐으면 스킵
                    continue
                if graph[ny][nx] == 1:          # 탐색하는곳이 칸막이라면 스킵
                    continue
                visited[ny][nx] = True
                ..
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 위가 내 코드인데, stack을 갑자기 넣어야할거같은데 (방문처리한곳을), dfs를 ㅡ안하고 순회해서 그게 안됨. 방향자체가 잘못되었음. --> dfs를 정의하면서 시작해야하는것 같다 ... -- > 아닌듯??????

# def dfs(y, x): #dfs에 변수가 두개들어간다 !
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False
#     if graph[y][x] == 0:
#         graph[y][x] = 1 # 방문처리..?
#         dfs(y - 1, x)
#         dfs(y, x - 1)
#         dfs(y + 1, x)
#         dfs(y, x + 1)   #상하좌우도 모두 재귀적으로 호출..
#         return True
#     return False
# result = 0
# for y in range(N):
#     for x in range(M):
#         if dfs(y, x) == True:
#             result += 1
# print(result)

# 인덱스 에러나오는데......