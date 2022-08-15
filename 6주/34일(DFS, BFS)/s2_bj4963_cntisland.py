# h x w 행렬이 주어짐 ( 입력은 w, h 순으로) // h개의 행렬이 입력됨. 1은 땅, 0은 바다, 입력의 마지막엔 0 0이 주어짐
# 팔방탐색을 해서 주변이 전부 바다인 땅이있으면, 섬 1개를 올림 ( 팔방탐색시 땅이 하나라도 더 있으면 같은섬)
# """
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 0 0
# """"
# 테스트 케이스 

import sys
sys.stdin = open('island.txt', 'r')


while True:
    w, h = map(int, input().split())
    if w == False and h == False:   # 0 0이 입력됐을떄 종료
        break
    
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    # print(graph)

    dy = [-1, -1, -1, 0, 0, 1, 1, 1] #좌상 상 우상 좌 우...
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0
    stack = []
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 0:        # 방문한 좌표거나 아예 바다인 좌표라면, 다음순회로 넘어감
                continue
            graph[y][x] = 0 # 방문처리
            stack.append((y, x))
            cnt += 1                   #방문한 좌표가 아니면서 바다가 아닐때, cnt 를 증가시킴.
            while stack:
                r, c = stack.pop()
                for d in range(8):
                    ny = r + dy[d]      # y,x를 사용하는게 아니고 스택에 등록된 좌표쌍을 사용함 (방문처리할때 스택에 등록하는 좌표쌍)
                    nx = c + dx[d]
                    if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
                        graph[ny][nx] = 0   #조건에 맞는영역을 팔방탐색했을때, 방문표시
                        stack.append((ny, nx))

    print(cnt)