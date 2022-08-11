#보드위에 킹 위치가 주어짐 . 말위치가 알파벳+숫자인데 알파벳 = 열 숫자 = 행 (A1 -> 1,1)
#킹이나 돌이 나가면 다음입력실행 // 마지막 이동후 좌표출력
import sys
sys.stdin = open('king.txt', 'r')

board = [[0] * 8 for i in range(8)]

dic_ = {
    'R' : (0, 1),
    'L' : (0, -1),
    'B' : (1, 0),
    'T' : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (1, -1),
    '8' : 0,
    '7' : 1,
    '6' : 2,
    '5' : 3,
    '4' : 4,
    '3' : 5,
    '2' : 6,
    '1' : 7
}

K, stone, N = input().split() # 킹 돌 위치와 이동횟수
co_K = []           #킹과 돌의 좌표 리스트
co_stone = []

co_K.append(ord(K[0]) - 65)
co_K.append(dic_[K[1]])
co_K = co_K[::-1]               # 좌표를 보기쉽게 변환


co_stone.append(ord(stone[0]) -65)
co_stone.append(dic_[stone[1]])
co_stone = co_stone[::-1]

for i in range(int(N)):                 # 돌과 킹이 따로이동하고 + 두개가 겹치면 안되고 + 킹이 이동하는곳에 돌이 있을때 같은방향으로 돌이 움직임..
    move = dic_[input()]
    if 7 >= move[0] + co_K[0] >= 0  and 7 >=  move[1] + co_K[1] >= 0:           #킹이 이동가능하고
        if 7 >= move[0] + co_stone[0] >= 0 and 7 >= move[1] + co_stone[1] >= 0:     #돌도 이동이 가능하고
            co_K[0] += move[0]
            co_K[1] += move[1]
            if co_K == co_stone:            #이동한 킹의 좌표가 돌의 좌표와 같을때, 돌을 같은방향으로 이동시킨다. 
                co_stone[0] += move[0]
                co_stone[1] += move[1]
    
        else:                       #킹은 이동이되는데 돌은 이동이 불가능하다면
            co_K[0] += move[0]
            co_K[1] += move[1]
            if co_K == co_stone:        #이동한 킹의 좌표가 돌의좌표와 겹친다면, 이동을 하지않는다 (원래좌표로 돌아간다)
                co_K[0] -= move[0]
                co_K[1] -= move[1]

## co_K ,co_stone이 평범하게 쓰이는 좌표로 나타남 ([7,0] , [6,0] 이런식) . 이걸 다시 변환해야하는데.. 

dic2 = {
    7 : '1',
    6 : '2',
    5 : '3',
    4 : '4',
    3 : '5',
    2 : '6',
    1 : '7',
    0 : '8' 
}


p_k = ['a', 0]
p_s = ['a', 0]
p_k[0] = chr(co_K[1] + 65)
p_k[1] = dic2[co_K[0]]

p_s[0] = chr(co_stone[1] + 65)
p_s[1] = dic2[co_stone[0]]
# print(p_k, p_s)


ans_k = ''.join(list(map(str,p_k)))
print(ans_k)
ans_s = ''.join(list(map(str,p_s)))
print(ans_s)