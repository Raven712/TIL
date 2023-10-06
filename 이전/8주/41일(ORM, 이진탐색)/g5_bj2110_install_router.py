#집이 n개 있음. 좌표가 xn.. 개있음. 공유기 c개 설치. 인접 공유기 사이 거리를 가능한 크게 설치하려함. c개의 공유기를 n개의 집에 적당히 설치해서 가장인저한 공유기 사이 거리를 최대로하기
import sys
sys.stdin = open('router.txt', 'r')
input = sys.stdin.readline

# n, c = map(int, input().split()) # 2 <= n < 20만 2 <= c <= n

# max_ = 0
# coord = [] # 좌표리스트
# for i in range(n):
#     coord.append(int(input()))
#     if i > max_:
#         max_ = i

# coord.sort()
# start = 0

# cnt = 0 # 설치된 공유기개수 .  mid 에 설치하고 양끝에 하나씩 설치해나간다 ? 
# mid = n // 2
# # 공유기 c개를 xn에 설치해야함. 
# while cnt != c:
#     for i in range(int(c / 2)): 
#         a = abs(coord[mid] - coord[i])
#         b = abs(coord[mid] - coord[-i])
#         if a > b:
#             length = b
#         else:
#             length = a

# 망한거같음

# 답
n, c = map(int, input().split())
coord = [] 
for i in range(n):
    coord.append(int(input()))

coord.sort()

start = 1 # 거리 차이의 최소값
end = coord[-1] - coord[0] # 거리차이의 최대값. 당연히 좌표 sort
answer = 0


while start <= end:
    mid = (start + end) // 2
    cur = coord[0]
    cnt = 1
    for i in coord:
        if i >= cur + mid:
            cnt += 1
            cur = i
    if cnt >= c:
        start = mid + 1
        result = mid        #  조건만족시 결과값에 mid를 넣어줌. 
    else:
        end = mid - 1
print(result)