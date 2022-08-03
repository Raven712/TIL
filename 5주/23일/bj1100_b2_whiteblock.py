#체스판이 8x8 크기. 검-흰 번갈아 칠해짐. 0,0 은 흰색임. 흰칸위의 말 갯수는?
#F 가 말있는판
#(0,0246)
#(1,1357) .. 이런식으로 흰칸임
board = []
temp = 0
for i in range(8):
    temp = list(input())
    board.append(temp)

count_F = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 != 0:
                continue
            else:
                if board[i][j] == 'F':
                    count_F += 1
        else:
            if j % 2 == 0:
                continue
            else:
                if board[i][j] == 'F':
                    count_F += 1
print(count_F)

