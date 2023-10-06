# 산술평균, 중앙값,최빈값, 범위 출력하기.

import sys
input = sys.stdin.readline

N = int(input())
list_ = []
for i in range(N):
    x = int(input()) #주어지는 값들의 ~~ 출력하기.
    list_.append(x)
sum_ = sum(list_)
list_ = sorted(list_)
if 0 > (sum_ / N) > -1:
    print(0)
else:
    print('{:.0f}'.format(sum_ / N))# 1

for i in range(N): 
    if i == int((1/2) * N): # +1해야하는데 리스트인덱스는 0부터라
        print(list_[i])
       
#2 중앙값
################################


dic_l = {}
for i in range(N):
    if list_[i] not in dic_l:
        dic_l[list_[i]] = 1
    else:
        dic_l[list_[i]] += 1
vin = list(map(list,dic_l.items()))

vin = sorted(vin)           #[[-2, 1], [1, 1], [2, 1], [3, 1], [8, 1]]
max_ = 0
cnt = 0
for i in range(len(vin)):
    if vin[i][1] > max_:
        max_ = vin[i][1]

list_cnt = [] # 최빈값을 리스트로 만들어서 여기서 두번째로 작은값을 출력해야됨 (최빈값이 여러개일때)
for i in range(len(vin)):
    if vin[i][1] == max_:
        cnt += 1
        list_cnt.append(vin[i][0])

if cnt >= 2:
    print(list_cnt[1])
else:
    for i in range(len(vin)):           #최빈값
        if vin[i][1] == max_:
            print(vin[i][0])

# print(vin)
# print(dic_l)

# for i in range(N):
#     if vin[i][1] > max_:
#         max_ = vin[i][1]

# for i in range(N):
#     if vin[i][1] == max_:
#         cnt += 1
##################################################


print(list_[-1] - list_[0]) # 범위