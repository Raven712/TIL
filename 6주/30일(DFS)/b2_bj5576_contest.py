# W, K 각각 10명씩 점수가 주어짐. 높은수 3개를 합산해서 누가높은지 비교하기

list_W = []
for i in range(10):
    W = int(input())
    list_W.append(W)

list_K = []
for i in range(10):
    K = int(input())
    list_K.append(K)

list_W.sort()
list_K.sort()

point_W = list_W[-1] + list_W[-2] + list_W[-3]
point_K = list_K[-1] + list_K[-2] + list_K[-3]

print(point_W, point_K)