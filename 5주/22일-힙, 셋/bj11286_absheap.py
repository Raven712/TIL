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