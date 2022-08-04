# N x N 행렬. 2자리 연속 흰색이어야함. 가로-세로 다 가능
# 근데 벽이나 짐에 닫아야함
# 문제이해가 잘안됨.... << 표현이 잘못된듯 문제가
# 연속된걸 찾으려면, 각 리스트속의 리스트가 연속인지아닌지 보면됨
#중간에 어중간하게 누운곳을 배제하고, ..X.. 같은것도 계산할수있어야함

N = int(input())
room = []                                                                                                      OOOOO < 1 OOOOX OOOXO OOXOO <<
for i in range(N):
    room.append(list(input()))  
blank = 0 # X아닌곳 넣을예정 . 값이 2가 되면 누울수있는라인이게됨

row = 0 # 누울수있는 가로,세로 줄 수 (행/열)
col = 0
                        [[.,.,.,.,X]. [...]]
for i in range(N):
    for j in range(N):
        if room[i][j] == '.':       # 가로갯수 세기. 블랭크가 (.갯수) 2가 되는순간 누울수있다 (row)를 1 증가시킴. 
            blank += 1
        else:
            blank = 0       # X를 만나면 초기화
        if blank == 2:      # . 갯수가 2가될때 누울수있는곳으로 판정(row += 1). 3이나 4나 5나 다 누울수있는건 매한가지 (고무인간이라고 생각해야할듯)
            row += 1
        if j == N - 1:      # 리스트속의 리스트 (하나의 행)가 끝날때 blank 를 초기화시키고 i+1 로 이동하고 j는 다시 0부터... 반복
            blank = 0

blank = 0

for i in range(N):
    for j in range(N):
        if room[j][i] == '.':       #세로개수 새기. 거의같음
            blank += 1
        else:
            blank = 0
        if blank == 2:
            col += 1
        if j == N - 1:              # 다만 얘는 각자다른 리스트의 i번째 인덱스를 보는거라서, i가 변할떄가 아닌 j가 N-1이 될때 (첫행부터 끝행까지 다 i번째 인덱스를 다 참고했을때) 
            blank = 0               # blank를 초기화시키고, i 는 i + 1이 되고, j는 0부터 시작.. 반복

print(row, col)


# 왜 얘들이 브론즈 1일까