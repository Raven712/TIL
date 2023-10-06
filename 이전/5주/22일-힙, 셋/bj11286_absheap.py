#리스트에 x넣기. 절대값 제일낮은거 출력하고 제거 ... 절대값이 작은게 여러개면 실제수가 작은걸 출력후 제거 .. 시작은 빈리스트

# 1. 그냥 아는대로 풀어보기
# N = int(input())
# list_ = []
# abslist_ = list(map(abs, list_))

# for i in range(N):
#     x = int(input())
#     if not False:
#         list_.append(x)
#         abslist_.append(abs(x))
#     else:
#         #어지러움


# 2. 힙써보기
# import heapq                                # 절대값이 가장 작은수를 출력하고 원래값을 배열에서 제거하는게 어렵다
# N = int(input())
# list_ = []
# abslist_ = []

# for i in range(N):
#     x = int(input())
#     min_abslist_ = min(map(abs, list_))
    

#     if x != 0:
#         heapq.heappush(list_, x)
#     else:                                                         #어려워서 보류
#         for i in list_:
#             if abs(i) == min_abslist_:
#                 abslist_.append(i)
#             if i == min(abslist_):
#                 print(i)
#                 heapq.heappop(list_)


## 풀이:
# heappush << 리스트를 넣으면 0번 인덱스부터 뭐가 더 큰지 순서대로 비교. ex) [0,2] [1,0] << 이면 0번인덱스 가 작은 0,2이 맨앞에 옴. [0,1] [0,2] 면 1번째 인덱스가 작은 [0,1] 이 오고..

# 그러니까 이 문제는 비교 첫쨰 우선순위인 절대값을 0번인덱스에, 1번인덱스에 실제값을 넣는식으로 해결가능

import heapq
n = int(input())
heap = []

root = heappop(heap)
print(root[1] # 값뺄때

heappush(heap,[abs(x), x]) # 값넣을때 < 이걸이용해서 다시 풀어보기

#그렇다면 최대힙은 어떻게 구현할까 ? 오늘 배운걸 기반으로해서.