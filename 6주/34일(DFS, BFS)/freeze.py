import sys
sys.stdin = open('freeze.txt', 'r')
# """"
# 4 5
# 00110
# 00011
# 11111
# 00000
# """"   위의 입력이 주어지고, 0은 물, 1은 칸막이. 사방 탐색을 해서 칸막이가 다 쳐져있으면, 얼음 1개가 추가된다. 얼음의 개수를 출력하는 문제

n, m = map(int, input().split())    # n x m 행렬

graph = []
for i in range(n):
    graph.append(list(map(int, input())))           #.strip() 을 해야한다고 하는데 차이를 모르겠음 (출력이 같음)

# print(graph)
# 그래프를 좌표마다 탐색..          ---> 이차원리스트를 탐색할떄, 탐색한 좌표 (y,x) 를 튜플로 스택에 추가해야함!!!! 
#그리고 stack.pop()도, stack에 튜플이 들어있으니 변수 두개를 할당해야함 
#--> r c = stack.pop()
#
dr = [0, 0, 1, -1] #동 서 남 북
dc = [1, -1, 0, 0]

cnt = 0
stack = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:    # 1(칸막이) -> 넘어가기 . 그리고 1을 방문표시로 사용할 예정 (True == 1)
            continue
        graph[y][x] = 1 #방문표시
        cnt += 1
        stack.append((y, x))
        print(stack)
        while stack:
            r, c = stack.pop()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
                    graph[nr][nc] = 1
                    stack.append((nr, nc))
# print(cnt)


# -- >> 꼭 dfs 함수를 정의해서 해야하는게 아니다??

        