# 테스트케이스 개수가 주어짐. 체스판은 i x i 이고, y,x는 나이트가 있는칸, r,c 는 이동하고싶은 칸이다.
import sys
sys.stdin = open('knight.txt', 'r')
from pprint import pprint
from collections import deque

T = int(input())

for i in range(T):
    i = int(input())
    graph = [ [0] * i for j in range(i) ]
    # pprint(graph)

    y, x = map(int, input().split())
    r, c = map(int, input().split())
    dy = [-1, -2, -2, -1, 1, 2, 2, 1] # 10시 11시 ...
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    # visited = [ [0] * i for j in range(i) ]  # 필요한가?
    queue = deque()
    if y == r and x == c:
        print(0)
    else:
        def bfs(y, x):
            global queue
            queue.append((y, x))
            cancel = 0

            while queue:
                a, b= queue.popleft()
                for d in range(8):
                    ny = a + dy[d]
                    nx = b + dx[d]
                    if 0 <= ny < i and 0 <= nx < i and graph[ny][nx] == 0:
                        graph[ny][nx] = graph[a][b] + 1
                        queue.append((ny, nx))
                        if ny == r and nx == c:
                            print(graph[ny][nx])
                            cancel = 1
                            break
                if cancel == 1:
                    break
        bfs(y, x)

    # if visited[a][b] != 0:  # 방문했다면 다음번으로 . 필요한것같다. graph[a][b]는 bfs를 돌아서 좌표를 + 1 시켜주면, 충분히 0이 아닐수있기 때문에..
    #     continue
    # visited[a][b] = 1 # 방문처리

    # queue.append((a, b))

    # while queue:
    #     m, n = queue.popleft()
    #     # if m, n == r, c:
    #     #     break
    #     for d in range(8):
    #         ny = m + dy[d]
    #         nx = n + dx[d]
    #         if 0 <= ny < i and 0 <= nx < i and visited[ny][nx] == 0:          #수정가능성
    #             visited[ny][nx] = 1
    #             graph[ny][nx] = graph[m][n] + 1
    #             queue.append((ny, nx))

    
    # bfs(y, x)
    # print(graph)


