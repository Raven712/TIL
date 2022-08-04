# 1,2,3 번컵 1번컵아래 공. 컵두개고른뒤 위치바꾸기. 공은 그대로

M = int(input())
list_ = [1, 0, 0] # 1은 공이 있음을 뜻함
for i in range(M):
    X, Y = map(int, input().split())
    list_[X - 1], list_[Y - 1] = list_[Y - 1], list_[X - 1]      #스왑?

for i in range(3):
    if list_[i] == 1:
        print(i + 1)

