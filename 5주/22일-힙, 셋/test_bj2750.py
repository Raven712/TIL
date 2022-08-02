import time
start = time.time()

N = int(input())
list_ = []
for i in range(N):
    x = int(input())
    list_.append(x)
list_ = sorted(list_)
for i in list_:
    print(i)

print('time :', time.time() - start)            # time : 7.502377033233643