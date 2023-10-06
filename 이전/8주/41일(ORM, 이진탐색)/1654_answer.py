# 랜선 n개 필요. k개가 따로 있음. 길이가 제각각임. 그걸 전부 같은길이의 n개 랜선으로 만들고싶어함. 최대 랜선 길이를 출력하라.
import sys
sys.stdin = open('cut.txt', 'r')

k, n = map(int, input().split()) # k개를 가지고있고 (n)11개가 필요함.

k_list = []
max_ = 0        #최대가 아닌 최소로 해야할것같음
for i in range(k):
    k_ = int(input())
    if k_ > max_:
        max_ = k_    # 미리 이진탐색 끝부분을 만들어둠
    k_list.append(k_)

# k_list.sort()

cnt = 0
start = 1
end = max_
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in k_list:
        total += (i // mid)
    
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

###### 기존

#가장 짧은길이인 1을 start, 긴 길이가 end로