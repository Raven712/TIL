# 떡 개수 n, 길이 m. 둘째줄엔 떡 개별 높이 주어짐. 높이 총합은 항상 m 이상임. 적어도 m 만큼의 떡을 집에가져가기 위해 절단기에 설정할 수 있는 높이 최대치는?
import sys
sys.stdin = open('ddeok.txt', 'r')

# n, m  = map(int, input().split())       # 떡은 4개고 6만큼의 떡을 가져가야됨

# ddeok = list(map(int, input().split()))

# sum_ = 0

# h = 0 #높이
# def slicing(x):
    
#     global sum_
#     for i in ddeok:
#         if i - x > 0:
#             sum_ += i - x
#         else:
#             continue
#     if sum_ >= m:
#         sum_ = 0
#         slicing(x + 1)
#     else:
#         print(x - 1)

# slicing(0)

################################
#답
# 이렇게 탐색범위가 클떄 for쓰면 시간초과남

n, m = map(int, input().split())

list_ = list(map(int, input().split()))

start = 0
end = max(list_) # 떡중 제일 긴걸 끝점으로 잡음

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 # 소숫점 값 버리는거라서
    for x in list_:
        if x > mid:
            total += x - mid # 떡 자르기
    if total < m:   # 자른 떡의 양이 요구한 수치 m보다 작으면, 더 많이 잘라야함 (왼쪽 탐색하기)
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
