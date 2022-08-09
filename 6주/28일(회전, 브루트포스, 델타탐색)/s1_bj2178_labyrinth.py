import sys
sys.stdin = open('미궁.txt', 'r')

#N x M 행렬, 1은 갈수있고 0은 못감. 1,1에서 N,M으로 갈때 최소 몇칸 이동해야하는가??  상하좌우 이동만 된다.

laby = []
N, M = map(int, input().split())

for i in range(N):
    laby.append(list(map(int,input())))


# dx = [0,0,-1,1]
# dy = [1,-1,0,0] #상하좌우 인줄알았는데 우좌상하였음....
dc = [0,0,-1,1]
dr = [-1,1,0,0] #상하좌우

x = 0
y = 0
count = 0
b = set() # 되돌아오는거 방지


for i in range(N):
    for j in range(M):
        for k in range(4):
            nx = i + dr[k]
            ny = j + dc[k]
            n_ = (nx, ny)
            if n_ not in b:
                b.add(n_)
            else:
                continue
            
            if 0 <= nx < N and 0 <= ny < N and laby[nx][ny] == 1:
                count += 1
                i = nx
                j = ny
            
print(count)
