# 딕셔너리의 값을 1씩 늘리는식으로 해서 특정 키(각)의 값으로 문제를 풀자.
# import sys
# sys.stdin = open('tri.txt', 'r')

# input = sys.stdin.readline

dic_ = {}
list_angle = []
for i in range(3):
    angle = int(input())
    if angle not in dic_:
        dic_[angle] = 1
    else:
        dic_[angle] += 1
    list_angle.append(angle)

if sum(list_angle) != 180:        #sum(dic_.keys()) # 이렇게하니까 딕셔너리에 각도가 같은게 들어가버리면 삼각형으로 인식을 안함
    print('Error')

else:
    if max(dic_.values()) == 3: # 삼각형의 각도가 전부 max치라면 (각도가 최대치(max)인 각이 3개라면)
        print('Equilateral')
    elif max(dic_.values()) == 2 or min(dic_.values()) == 2: # 삼각형 각도의 최대치가 2개로 나오거나 최소치가 2개로 나온다면  (즉 삼각형에서 같은각이 두개)
        print('Isosceles')
    elif max(dic_.values()) == 1 and min(dic_.values()) == 1: # 삼각형 각도 최대치가 1개이면서 최소치가 1개라면 (나머지는 최소도 최대도 아닌각을 가졌다면)
        print('Scalene')