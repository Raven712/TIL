# 2차원에 N개점 주어짐. x좌표 증가하는순으로, x같으면 y가 증가하는순으로 정렬해서 출력하기.
import sys
sys.stdin = open('좌표정렬.txt', 'r')

N = int(input())

list_ = []
for i in range(N):
    S = list(map(int, input().split())) # S = [x, y]
    list_.append(S)
    
list_ = sorted(list_)

for i in list_:
    a, b = i[0], i[1]
    print(a, end = ' ')
    print(b)
    # for j in i:             #이중 for문을 쓰면 느려지는데, 이차원리스트안의 각각의 리스트를 대괄호만 없이 출력하는법은 없을까?? 위처럼 하면 되겠다
        
        