import sys
sys.stdin = open('truck.txt', 'r')

#트럭 3대 보유. 주차트럭수따라 할인. 한대 댈떄 a 두대 b 세대 c원 내야함 (분당). 주차요금 출력
#리스트 등록한뒤 제일늦은 주차시작시간 - 제일 빠른 나간시간 해보기.

A, B, C = map(int, input().split())
list_ = []
list_arr = []
list_leave = []

for i in range(3):
    arr, leave = map(int, input().split())
    list_.append([arr, leave])
    list_arr.append(arr)
    list_leave.append(leave)
    
sum_ = 0
cnt = 0 






# if max(list_arr) <= min(list_leave):
#     if cnt == 0:
#         sum_ += (min(list_leave) - max(list_arr)) * A
#         list_leave.remove(min(list_leave))
#         cnt += 1
#     elif cnt == 1:
#         sum_ += (min(list_leave) - max(list_arr)) * B
#         list_leave.remove(min(list_leave))
#         cnt += 1
#     elif cnt == 2:
#         sum_ += (min(list_leave) - max(list_arr)) * C
#         list_leave.remove(min(list_leave))

# else:
