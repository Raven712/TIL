#성적 주어졌을때 최대점수 최소점수 점수차이 3개를 구하는프로그램

from collections import deque

K = int(input()) #반 갯수

for i in range(1, K + 1):
    N = list(map(int, input().split())) # 학생수가 첫번쨰입력, 그뒤로는 입력된 학생수만큼 점수가 입력됨

    print(f'Class {i}')

    # point = [] # N에서 첫째입력빼고 넣을것
    # for j in range(1, len(N)):
    #     point.append(N[j])                    !!  이렇게하면 느리니까 deque을 써보자. !! 
    
    point = deque(N)
    point.popleft()
    point = list(point)
    # print(point) < 점수만 달린 리스트가 됐다

    #Largest gap은 각각의 점수대별 갭.. 중 제일 큰것 ( 10, 20 ,50, 70, 80) 이 있으면 20->50의 격차가 30으로 제일크므로 라지스트갭은 30이됨

    point = sorted(point)       # 위를 위해 포인트를 정렬했음. 
    gap = 0
    for j in range(len(point)):
        if j == 0:
            gap = 0
        else:
            if point[j] - point[j - 1] > gap:
                gap = point[j] - point[j - 1]

    print(f'Max {max(point)},', end = ' ')
    print(f'Min {min(point)},', end = ' ')
    print(f'Largest gap {gap}')


