# 0은 집x 1이 집임. 사방탐색을 통해 연결된곳이 있냐없냐를 확인, 사방이 전부 0이면 단지가 끊김 .(하나의 단지)
# 단지수를 출력하고, 집 갯수도 출력하기(단지당 집 개수. 오름차순)

import sys
sys.stdin = open('num.txt', 'r')
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

# print(graph)
# [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

dy = [-1, 1, 0, 0] #상 하 좌 우
dx = [0, 0, -1, 0]


# dic_ = {}
cnt_danji = 0 # 단지의 수
cnt_house = 0 # 단지내의 집의 수
list_cnt_house = []
stack = []
# visited = [ [False] * n for i in range(n) ]
for y in range(n):
    for x in range(n):
        if graph[y][x] == 0:    # 집이 아니거나 방문한곳이면 다음곳으로
            continue
        stack.append((y, x))            #스택에 좌표를 튜플로 넣는다..
        graph[y][x] = 0      
        cnt_house = 1
        cnt_danji += 1
        while stack:
            r, c = stack.pop()
            for d in range(4):
                ny = r + dy[d]
                nx = c + dx[d]
                if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:              <<<< 이 방법은 bfs로 해야하는것 같다.
                    graph[ny][nx] = 0       #0으로 만드는것으로 방문처리...
                    stack.append((ny, nx))
                    cnt_house += 1
        
print(cnt_danji, list_cnt_house)

