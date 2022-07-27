total = []             #단순 덧셈이 아니라 비교라서 리스트가 편할것같았음
point2 = 0            # 총점을 기록할 변수
for i in range(10):
    point = int(input())

    if i == 0:              #아래의 코드에서 [i -1] 범위가 있어서, i == 0일때 따로 설정을 해줘야했음. 점수는 입력값, 총점인 point2도 누적
        total.append(point)
        point2 += point
    else:
        point2 += point
        total.append(point2)
        if total[i] >= 100 and total[i - 1] <= 100:
            if total[i] - 100 <= abs(total[i - 1] - 100):
                print(total[i])
                break
            else:
                print(total[i - 1])
                break
        
    if i == 9:
        print(total[9])    