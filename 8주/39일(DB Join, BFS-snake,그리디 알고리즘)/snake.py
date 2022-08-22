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
    dic_ladder[x] = y


for i in range(m):
    u, v = map(int, input().split()) # 뱀의 정보. u번칸에 가면 v번칸으로 간다. 
    dic_snake[u] = v
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


# 딕셔너리는 위처럼 등록하고, 큐를 좌표 튜플로 등록하는게 아니고 진짜 번호를 넣는다 (그냥 하나의 숫자) --> visited도 그냥 [False] * 100 혹은 101 하면됨.
# 주사위는 그냥 range(1,7) 로 표현하면 됨. (for d in range(4) 를 대신하는 느낌임.) v
# 이중 if문을 쓴다. 왜냐면 뱀과 사다리가 있는칸에 갔냐 + 방문 안헀냐 두개의 선행조건을 걸고 (첫 if), 사다리인 경우 - 뱀인 경우 - 그리고 사다리+뱀+그냥 전부다(여기서 if not visited로 2차 if문) 해서
# 1차if문에서 범위조건과 미방문조건을 충족시켰을떄 -> 사다리 태우거나 뱀 태우거나 그냥 주사위 굴림 -> 다시 미방문조건을 확인해서 방문표시와 주사위돌린 횟수를 추가하며 q.append 함...