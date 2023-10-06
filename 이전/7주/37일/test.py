n = int(input())

graph = [list(map(int,input().strip())) for i in range(n)]
# print(graph)
# [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]

cnt = 0
cnt2 = 0
queue = deque()
dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]

list_ = []

for y in range(n):
    for x in range(n):
        if not graph[y][x]:
            continue
        queue.append((y, x))    #큐에넣기
        graph[y][x] = 0     #방문
        cnt2 =1
        while queue:
            r, c = queue.popleft()
            for d in range(4):
                ny = r + dy[d]
                nx = c + dx[d]
                if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
                    graph[ny][nx] = 0 #방문처리
                    queue.append((ny, nx))  #큐에 넣기
                    cnt2 += 1
        cnt += 1
        list_.append(cnt2)