## 손못대서 답지봄

#달팽이는 우하좌상으로 움직임

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    list_ = []
    dx = [1, 0, -1, 0] #우하좌상
    dy = [0, 1, 0, -1]
    for j in range(N):
        list_.append([0] * N)

        r, c = 0, 0
        dist = 0
        
    for j in range(1, N*N + 1): # << 그냥 행렬전체를 탐색하는건데 되게좋은듯
        list_[r][c] = j
        r += dy[dist]
        c += dx[dist]
        # 여기서 0이아닌 다른값이 있거나 범위밖으로 가거나 하면 dist를 바꿔주는식..
        if r< 0 or c < 0 or r >= N or c >= N or list_[r][c] != 0:  #r<0 c<0 은 왜 들어가지 -->  N x N 에서 음수가되면 범위밖이라
            r -= dy[dist]
            c -= dx[dist]
            dist = (dist + 1) % 4

            r += dy[dist]
            c == dx[dist]
    for k in list_:
        print(*k)