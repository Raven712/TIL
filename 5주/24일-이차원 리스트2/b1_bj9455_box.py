#조건1 : 현재박스 아래에 박스가 없어야함
#조건2 : 박스는 바닥을 벗어나면 안됨 (인덱스가 리스트를 벗어나면안됨)    << 이것떄문에 애초에 


T = int(input())
for test_case in range(T):
    m, n = map(int, input().split())    # m n =5,4 
    box = 1
    empty = 0
    if box_list[y + 1][x] != box:   #조건1
    if y + 1 != m: #조건2
    count = 0 #이동거리

while box_list[y + 1][x] != box and y + 1 != m:  #현재박스 아래에 박스가 없으면서 / 박스가 바닥을 벗어나지 않는다면 반복한다


#열 우선순회, 이중반복

    for x in range(n):
        for y in range(m)[::-1]:    # 박스를 아래에서부터 봐야해서 거꾸로봐야함. [::-1] 을 하거나  reversed(range(m)) 하면됨
    #여기서, 만약 현재 탐색중인 좌표에 박스가 있으면
        if box_list[y][x] == box:
            while y + 1 != m and box_list[y + 1][x] != box :     #while 쓸땐 앞에있는것부터 검증을 함. 그래서 box_list[y+1] 에서 box_list[5][x] < 이게 나와서, 조건을 while y+1 != m << 이것부터 해야함
                box_list[y][x] = empty                              #범위부터 먼저 확인하자 . 굳이 while뒤에 조건문을 다 쓰기보다,
                                                                    # while True: // if y + 1 != m: // if box_list[y+1][x] != box: 이렇게 해도됨
                box_list[y+1][x] = box
                y += 1
                count += 1

            #조건1, 박스아래에 박스가 없어야함
            # box_list[y + 1][x]
            #조건2, 바닥 안벗어나야함
            # and y + 1 != m:
            #근데 이때 반복을 해야하므로 (무한으로) < while사용
