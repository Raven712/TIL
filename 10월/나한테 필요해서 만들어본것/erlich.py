import random
from collections import Counter
list_ = []
for i in range(100000):
    cost = 500000
    weight = [0.02, 0.98]
    cnt = 0
    erlich = 0
    realcost = 0
    while cnt <= 100 and erlich == 0:
        cnt += 1
        realcost += cost
        temp = random.choices([0, 1], weight)
        if temp[0] == 0:
            erlich += 1
        else:
            continue
    list_.append(realcost)

sum_ = 0
for i in list_:
    sum_ += i

avg = sum_ / 100000

print(avg)

# weight = [0.4, 0.6]
# a = random.choices([0, 1], weight)
# print(a)