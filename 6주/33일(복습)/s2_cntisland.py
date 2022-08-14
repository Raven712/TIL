# 풀었던 문제지만 하루 쉬었고 복습느낌으로 새로 풀어보려고 함.
# 섬과 바다지도가 주어짐. 1은 땅이고 0이 바다. 8방에 바다만 있으면 독립된 섬이고 땅이있다면 하나의섬으로 취급.
import sys
sys.stdin = open('is.txt', 'r')

while True:
    w, h = map(int, input().split())        #w은 너비 (열) h는 높이( 행) -- > h x w 행렬이다.

    if w == 0 and h == 0:
        break
    
    graph = [ [0] * (w) for i in range(h)]
    # print(graph)
    for i in range(h):
        graph_idx = list(map(int, input().split()))   #지도가 주어짐. graph idx는 지도의 한 행에 해당함.
        for j in range(w):
            graph[i][j] = graph_idx[j]     #그래프를 입력된것처럼 보이게해줌
    # print(graph)

    dx = [-1, 0, 1, -1, 1, -1, 0, 1] #좌상 상 우상 좌 우 ...
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    #델타이동을 하면서, 0만 있으면 섬 갯수를 늘리고, 땅이있다면 섬개수 유지..? ㄴㄴ dfs를 써서 확인해야할것같음. 인접 리스트는 어떻게 만들까?
    # graph_list = [[0] * w for i in range(h)]
    # cnt_adj = 0
    # for y in range(h):
    #     for x in range(w):
    #         if graph[y][x] == 0: 
    #             graph_list[y][x] = 'sea'
    #             continue
    #         for d in range(8):
    #             nx = x + dx[d]
    #             ny = y + dy[d]
    #             if 0 <= nx < w and 0 <= ny < h:
    #                 if graph[ny][nx] == 1:
    #                     graph_list[y][x] += 1
    
    # print(graph_list)

# 이 문제는 주어진 이차원 그래프를 그대로 dfs로 탐색해야하는 문제인듯함. 즉 visited =가 False로 h x w 만큼 차있는걸 만들고, 탐색시켜야함.

    visited = [[False] * w for i in range(h)]           # 이거할떄, False에 []를 해주지않으면 0으로 인식되버린다. 즉 숫자 0과 w를 곱한값으로 인식해버림

    ######################
    # print(visited)
    dic_graph = {}  ## 이차원리스트를 인접리스트로 표현하기위해선 딕셔너리가 꼭 필요한것같다!!!!. << 이게 핵심
    #####################


    for y in range(h):
        for x in range(w):
            if graph[y][x] == 0:
                continue
            if visited[y][x]:  #방문처리가 됐다면 올필요 없는것 같다.
                continue
            dic_graph[(y,x)] = []
            for d in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < h and 0 <= nx < w:
                    if graph[ny][nx] == 0:  #바다는 고려하지않음.
                        continue
                    dic_graph[(y, x)] += [(ny, nx)] #이부분이 생소하니 반복을 하도록 하자

    # print(dic_graph)
    def dfs(start : tuple):
        stack = [start]
        visited.append(start)       #시작정점 방문처리라고 하는데, 이게 왜 시작정점 방문처리인지 모르겠음. ( True 로 바꿔야하는것 아닌가)
        while stack:
            cur = stack.pop()
            for adj in dic_graph[cur]:
                if adj not in visited:
                    visited.append(adj)
                    stack.append(adj)
    # 이 방법은 visited의 False를 True로 바꾸는게 아니고, 좌표를 추가하고 좌표가 있는지없는지를 확인하는것으로 방문여부를 체크하는 방법같다.

    cnt = 0
    for i in dic_graph:
        if i not in visited:
            dfs(i)
            cnt += 1
    print(cnt)

    #복습 반드시 필요함
