
# 직사각형 넓이 구하기. 전부다 구해서 중복을 빼거나.. 따로구하거나
# 좌표xy는 100100 이하. 1사분면
# 그런데 입력은 x y i j << 로 주어지는데 xy는 왼쪽아래좌표 ij는 우측상단 좌표임

# 풀이 1. 좌표를 0으로 바꾼뒤, 넓이를 구해야하는곳만 1로 바꿔서 전부다 더하는 방법.

# 여기서, 100x100 행렬을 만드는것은 .. 리스트컴프리헨션으로 굉장히 간단하게 가능함.

# board = [[0 for i in range(101)] for j in range(101)] ??

board = [[0 for i in range(101)] for j in range(101)]


for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1 # << 이렇게하면 겹치든말든 1이되니까 상관없다
answer = 0
for row in board:
    answer += sum(row)
print(answer)