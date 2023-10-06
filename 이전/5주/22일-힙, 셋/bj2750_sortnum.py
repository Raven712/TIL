import time
start = time.time()

import heapq
heap_ = []
N = int(input())
for i in range(N):
    x = int(input())
    heapq.heappush(heap_, x)

for i in range(N):
    print(heapq.heappop(heap_))         # heap으로 풀었는데 시간차이가 있을까 ??
print('time :', time.time() - start)                       # time : 7.435937881469727


# import time
# start = time.time()

# N = int(input())
# list_ = []
# for i in range(N):
#     x = int(input())
#     list_.append(x)
# list_ = sorted(list_)
# for i in list_:
#     print(i)

# print('time :', time.time() - start)            # time : 7.502377033233643

