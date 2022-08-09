# #빌딩 X주차됨 .주차안됨 차는 2행2열 부숴야하는 차 수 세기 빌딩은 ㄴㄴ ////  그냥 댈수있는공간 개수, 1대,2대,...,4대 부수고 댈수있는 공간개수 따로따로 출력하기.
import sys
sys.stdin = open('monster.txt', 'r')

R, C = map(int, input().split())
map_ = []
for i in range(R):
    word = input()  #길이 C
    map_.append(list(word))

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1] #제자리 우 하 우하
cnt1 = 0 #부숴야하는 차 갯수
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt0 = 0

stop = True
for r in range(R):
    for c in range(C):
        cnt = 0 # . 갯수
        cntX = 0 # X 갯수
        # if map_[r][c] == '.':
        #     cnt += 1
        for d in range(4):        
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                # r = nr
                # c = nc
                if map_[nr][nc] == '.':
                    cnt += 1
                elif map_[nr][nc] == 'X':
                    cntX += 1
                else:
                    cnt = 0
                    cntX = 0
                    break
        # elif map_[r][c] == 'X':
        #     cntX += 1
        #     for d in range(3):        
        #         nr = r + dr[d]
        #         nc = c + dc[d]
        #         if 0 <= nr < R and 0 <= nc < C:
                    
        #             # r = nr
        #             # c = nc
        #             if map_[r][c] == '.':
        #                 cnt += 1
        #             elif map_[r][c] == 'X':
        #                 cntX += 1
        #             else:
        #                 cnt = 0
        #                 cntX = 0
        #                 break
        # else:
        #     break
            
        if cnt == 4:
            cnt0 += 1
        elif cnt == 3 and cntX == 1:
            cnt1 += 1
        elif cnt == 2 and cntX == 2:
            cnt2 += 1
        elif cnt == 1 and cntX == 3:
            cnt3 += 1
        elif cntX == 4:
            cnt4 += 1
        

print(cnt0)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)