# m x n 행렬. 박스를 내릴수있는 제일아래까지 내리고 이동거리구하기
# 

T = int(input())
for test_case in range(T):
    m, n = map(int, input().split())
    grid = []
    count = 0 #이동거리

    for i in range(m):
        N = list(map(int,input().split()))      # m x n 행렬 grid 만들기
        grid.append(N)
    
    temp = 0

    for i in range(n):
        for j in range(m)[::-1]:
            if grid[j][i] == 1 and :
                for k in range(m)[::-1]:
                    if k != j and grid[k][i] == 0:
                        grid[k][i] = grid[j][i]
                        count += k - j
                        grid[j][i] = 0
                        
print(count)
                        

GG
