# n x n격자. 지뢰 m개. 0은 빈곳. 숫자는 주변지뢰수
#행렬두개를 비교해서 열린곳은 숫자를 안열린곳은 .으로 막아두기
#지뢰밟았으면 모든곳이 * 로 출력

# '행렬의 인접요소가 지뢰라면 / 아니라면을 어떻게 표현하지 <<

n = int(input())
board = [] #지뢰위치 표시
for i in range(n):
    line = list(input())
    board.append(line)

p_board = []  # 연곳과 안연곳 표시
for i in range(n):
    line2 = list(input())
    p_board.append(line2)

a= [0] * n
on_board = []
for i in range(n):
    on_board.append(a)
                         #출력될 보드
   #지뢰밟은 보드 = 그냥 보드


for i in range(n):
    for j in range(n):
        if p_board[i][j] == '.':    # 안열어봤다면 출력할떄 '.'
            on_board[i][j] = '.'
        else:                         # 열었다면
            if board[i][j] == '*':  #그게 지뢰라면, 지뢰보드 출력할예정
                on_board = board
            else:
                
# '행렬의 인접요소가 지뢰라면 / 아니라면을 어떻게 표현하지 << 여기서 막혀서 GG