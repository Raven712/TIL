A = list(map(int, input().split()))
B = list(map(int, input().split()))
point_A = 0
point_B = 0

for i in range(10):
    if A[i] > B[i]:
        point_A += 3
    elif A[i] == B[i]:
        point_A += 1
        point_B += 1       
    else:
        point_B += 3             # 점수 총점 계산
print(point_A, point_B)

if point_A > point_B:
    print('A')                  # 이후 A가 점수더높으면 A출력
elif point_A == point_B:
    if A == B:                  # 같을떄는. ..일단 전경기 드로우일때 D 출력, 나머지는 마지막에 이긴사람을 확인해야 하는데 ....
        print('D')
    else:
        for i in range(9, 0, -1):   #역순으로 순회해서 큰게 나오면 큰쪽을 출력하고 종료
            if A[i] > B[i]:
                print('A')
                break
            if A[i] < B[i]:
                print('B')
                break
else:
    print('B')