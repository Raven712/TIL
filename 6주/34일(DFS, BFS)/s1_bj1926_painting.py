#그림이 이차원 리스트로 주어지는데, 그림의 개수와 넓이가 가장큰것의 넓이를 출력 ( 그림 = 대충 섬의개수의 섬같은 개념 )
#그림은 1이 그림이고 0은 그냥 도화지
import sys
sys.stdin = open('painting.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())  # n x m 행렬의 도화지

graph = [list(map(int, input().split())) for i in range(n)]
# print(graph)

cnt = 0
stack = []


dy = [-1, 1, 0, 0] #상하좌우
dx = [0, 0, -1, 1]
width_max = set()
width = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:    #도화지거나 방문했다면 다음순회로
            continue
        graph[y][x] = 0 #방문처리
        stack.append((y, x))
        cnt += 1
        width_max.add(width)
        width = 1
        while stack:
            r, c = stack.pop()
            for d in range(4):
                ny = r + dy[d]
                nx = c + dx[d]
                if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    stack.append((ny, nx))
                    width += 1
                    # print(width)
                    width_max.add(width)
if cnt != 0:
    print(cnt)
    print(max(width_max))
else:
    print(0)
    print(0)

# 5 6
# 1 1 1 1 1 0
# 0 0 0 0 1 0
# 0 0 0 0 0 0
# 1 1 1 0 0 0
# 0 1 0 0 0 0           반례
