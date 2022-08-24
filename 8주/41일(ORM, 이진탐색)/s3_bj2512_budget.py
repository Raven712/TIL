# 총 예산을 1. 요청 배정가능할시 그냥 배정 , 안되면 특정한 상한액을 계산하여 그 이상의 요청엔 상한만 배정. 상한이하는 그대로 배정.

import sys
sys.stdin = open('budget.txt', 'r')

n = int(input()) #지방의 수

budget = list(map(int, input().split())) #길이 n

lim = int(input())

start = 0
end = max(budget)

while start <= end:
    sum_ = 0
    mid = (start + end) // 2
    for i in budget:
        if i <= mid:
            sum_ += i
        else:
            sum_ += mid
    if sum_ <= lim:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)              # 왜 149가 나오지