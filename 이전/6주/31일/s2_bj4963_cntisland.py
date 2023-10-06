# 1은 땅 0은 바다. 섬은 주변이 0으로 뒤덮힌 1. 만약 팔방중 한군데가 땅이라면, 동일한 섬으로 취급함. 섬 개수 출력하기.
# 이건 dfs로 푸는건가 ??? (델타탐색은 힘들어보임..) 그리고 링크드리스트 갯수구하는것과 비슷해보임
# 델타탐색을 해서 단순 이차원배열에서 인접리스트를 뽑아냄 -> 인접리스트를 이용해서 dfs를 사용. dfs를 몇번썼는지를 출력하는 문제임...!!!!

import sys
sys.stdin = open('is.txt', 'r')


while True:
    w, h = map(int, input().split()) # 지도가 h x w 행렬임.
    if w == 0 and h == 0:
        break

    dh = [-1, -1, -1, 0, 0, 1, 1, 1] #좌상 상 우상 좌 우 좌하 하 우하
    dw = [-1, 0, 1, -1, 1, -1, 0, 1]

    map_ = []
    for i in range(h):
        _ = list(map(int, input().split()))     
        map_.append(_)
    # [[1,0,1,0,0], [1,0,0,0,0] ...] -> h x w 행렬

    visited = [[False] * w for i in range(h)]
    dic_ = {}   # 단순 이차원리스트를 인접리스트로 바꾸기위해서 이차원리스트를 돌면서 각좌표마다 인접한 땅들을(정점들을) 딕셔너리에 등록함!!!!!

    for i in range(h):
        for j in range(w):
            if not map_[i][j]:      # map_이 바다일떄 0 땅일때 1이니까 not 0(바다) --> True가 되어서, if문이 실행됨. 즉 바다일때 continue가 실행되서 반복문을 돌지않음
                continue
            if visited[i][j] == True:
                continue
                       
            visited[i][j] = True
            dic_[(i, j)] = []           # 딕셔너리의 내용물을 좌표튜플로 만들어둔다 (방문한 좌표를 키로 하는..)

            for d in range(8):
                nh = i + dh[d]
                nw = j + dw[d]
                if 0 <= nh < h and 0 <= nw < w and map_[nh][nw] != 0:           #범위조건을 만족하면서 탐색한 영역이 바다가 아닐떄(땅일때)
                    dic_[(i, j)] += [(nh, nw)]                      # 딕셔너리에 인접좌표중 범위조건을 만족하면서 땅인곳을 밸류로 추가시킨다!!!!!!! 

                    # if map_[i][j] == 1 and map_[nh][nw] == 0:      
                    #     cnt += 1     망한코드


    # print(dic_)
    # {(0, 0): [(1, 0)], (0, 2): [], (1, 0): [(0, 0), (2, 0)], (2, 0): [(1, 0), (3, 0)], (2, 2): [(3, 3)], (2, 4): [(3, 3)], (3, 0): [(2, 0)], (3, 3): [(2, 2), (2, 4)]}

    visited = [] # visited를 초기화시킴. 

    def dfs(start:tuple):           # 튜플을 넣을때는 튜플넣는다고 이렇게 알려야하는듯??? 
        stack = [start]
        visited.append(start)       # dfs는 for문으로 반복시키기떄문에 . 
        while stack:
            cur = stack.pop()

            for adj in dic_[cur]:
                if adj not in visited:              #딕셔너리라서 if not visited[adj] 이런게 아니고 그냥 딕셔너리에 없다면으로 해야함. 
                    visited.append(adj)     #이것도 visited[adj] = True 이런거 아님
                    stack.append(adj)


    cnt = 0

    for i in dic_:
        if i not in visited:
            dfs(i)
            cnt += 1

    print(cnt)
    