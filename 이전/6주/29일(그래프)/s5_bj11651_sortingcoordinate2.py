import sys
sys.stdin = open('좌표2.txt', 'r')

#2차원평면위 점 N개가 주어지고 좌표를 y좌표 증가하는순으로, y좌표가 같으면 x좌표가 증가하는순으로 출력하기
#y축값을 따로뽑아서 정렬하고 좌표가 그 y값을 갖고있을때 

N = int(input())
list_ = []
for i in range(N):
    x, y = list(map(int, input().split())) # S = [x, y]
    list_.append([y, x]) ## 이게되네

list_.sort()

for i in range(N):
    list_[i][0], list_[i][1] = list_[i][1], list_[i][0]

for i in list_:
    a = i[0]
    b = i[1]
    print(a, end = ' ')
    print(b)