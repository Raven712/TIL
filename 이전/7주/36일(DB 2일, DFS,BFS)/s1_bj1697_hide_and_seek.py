#수빈이랑 동생이 숨바꼭질. 둘은 서로다른 점에 있음. 수빈이는 걷기 , 순간이동 가능. 걸으면 X-1, X+1로 이동가능, 순간이동은, 2*X로 이동.
from collections import deque

x, k = map(int, input().split())
time = 0
# def move(point):
#     global time
#     if point > k:
#         time += 1
#         return point - 1
#     elif point < k:
#         time += 1
#         return point + 1

# def blink(point):
#     global time
#     if point < k :
#         time += 1
#         return point * 2

queue = deque()

while x != k:
    if x * 2 < k:
        x = x * 2
        time += 1
    elif x * 2 > k and (x - 1) * 2 >= k:
        x = x - 1
        time += 1
    elif x * 2 == k:
        x = x * 2
        time += 1
        break
    elif x + 1 == k:
        x = x + 1
        time +=1
        break
    elif x - 1 == k:
        x = x - 1
        time += 1
        break
print(time)