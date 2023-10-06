# 직사각형 4개있음. 4개 겹치기 가능. 넓이 합은?
#입력 4개. 1,2는 왼쪽아래좌표, 3,4는 우측상단 좌표.
# 사각형 넓이를 다 더한뒤에, 겹치는 영역을 다 뺴주자.. !! 
# 이중리스트의 0,1이 다른리스트의 0,1보다 크면서 2,3보다 작다면 리스트의 0,1~다른리스트의 2,3 까지의 넓이를 뺸다. 그리고 그중 한개만 넣는다 ...


def rectangle(a, b, c, d):
    return (c - a) * (d - b)


rec_sum = []
rec_square = [] #사각형넓이합
rec_square_ = [] #뺄넓이(중복)
for i in range(4):
    rec = list(map(int,input().split()))
    rec_sum.append(rec)
    rec_square.append(rectangle(rec[0],rec[1],rec[2],rec[3]))

for i in range(4):
    for j in range(4):
        if i != j:
            if rec_sum[j][2] >= rec_sum[i][0] >= rec_sum[j][0] and rec_sum[j][3] >= rec_sum[i][1] >= rec_sum[j][1]:
                rec_square_.append(rectangle(rec_sum[i][0], rec_sum[i][1], rec_sum[j][2], rec_sum[j][3]))

print(rec_square)
print(rec_square_)


GG