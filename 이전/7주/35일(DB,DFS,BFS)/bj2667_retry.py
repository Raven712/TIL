import sys
# sys.stdin = open('num.txt', 'r')
input = sys.stdin.readline


from collections import deque

n = int(input())

graph = [list(map(int, input().strip())) for i in range(n)]

# print(graph)
# [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

queue = deque()
cnt = 0         # 단지 수
cnt_house = 0   # 단지 내 집 수
list_house = [] # 을 리스트에 넣은것
dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]

for y in range(n):
    for x in range(n):
        if graph[y][x] == 0:
            continue
        queue.append((y, x))
        graph[y][x] = 0
        cnt += 1
        cnt_house = 1
        while queue:
            r, c = queue.popleft()
            for d in range(4):
                ny = r + dy[d]
                nx = c + dx[d]
                if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
                    graph[ny][nx] = 0 #방문처리
                    cnt_house += 1
                    queue.append((ny, nx))
        # cnt += 1
        list_house.append(cnt_house)
list_house.sort()
print(cnt)
if list_house:
    for i in list_house:
        print(i)
else:
    print(cnt)
