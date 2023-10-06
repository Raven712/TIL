# 뱀과 사다리게임. - 주사위를 조작해 내가원하는 수가 나오게 한다면, 최소 몇번만에 도착점에 도착할까. --> bfs.
# 게임크기가 10x10. 판에는 1~100까지 순서대로적힘. 주사위 굴려서 나온만큼 이동. 100을 넘으면 이동불가. 도착한 칸이 사다리면, 올라감. 뱀을 만나면, 내려감. --> 사다리타면 기존번호보다 크고, 뱀만나면 작아짐.
# 목표는 1번스타트에서 100번에 도착하기. 최소몇번 주사위 굴림?  +  100번칸에 무조건 도착하는 입력이 주어짐.
import sys
sys.stdin = open('snake.txt', 'r')
input = sys.stdin.readline
from pprint import pprint
from collections import deque

n, m = map(int, input().split()) #사다리와 뱀의 수. 1~15개

graph = [ [0] * 10 for i in range(10) ]
visited = [ [0] * 10 for i in range(10) ]
print(graph)
cnt = 1
for i in range(10):
    for j in range(10):
        graph[i][j] = cnt
        cnt += 1
# pprint(graph)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
#  [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
#  [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
#  [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
#  [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
#  [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
#  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
#  [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]

dice = [1, 2, 3, 4, 5, 6]
dic_ladder = {}
dic_snake = {}
for i in range(n):
    x, y = map(int, input().split())   # 사다리의 정보. x번칸에 도착하면 y번칸으로 간다
    


for i in range(m):
    u, v = map(int, input().split()) # 뱀의 정보. u번칸에 가면 v번칸으로 간다. 
    set_snake.add((u, v))
# print(set_ladder)
# print(set_snake)

queue = deque()
cnt = 0
me = 0
queue.append((0, 0))
cancel = 0
while queue:
    r, c = queue.popleft()
    for i in dice:
        if c + i <= 9:
            nr = r
            nc = c + i
        else:
            nr = r + 1
            nc = c + i - 10
        if 0 <= nr < 10 and 0 <= nc < 10 and (nr, nc) not in set_ladder and (nr, nc) not in set_snake:
            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))
            if nr == 9 and nc == 9:
                cancel = 1
                break
        elif (nr, nc) in set_ladder:

    if cancel == 1:
        break
print(visited)


#### 못풀겠음.
#어디서 막혔는가 ? --> dy, dx가 좌표의 형태로 주어지지않은점. 그래프도 마찬가지 (사다리와 뱀을 어떻게 딕셔너리에 등록시켜야할지 모르겠음. 방법은 보이는데 시간복잡도가 너무높아서 쓰면안될것같음)