A, B = map(int,input().split())

list_ = []
for i in range(1,46):
    for j in range(i):
        list_.append(i)


sum_A = 0
sum_B = 0
for i in range(len(list_)):
    sum_A += list_[i]
    if A == 1:
        A = 0
        break
    if i == A - 2:
        break
for i in range(len(list_)):
    sum_B += list_[i]
    if i == B - 1:
        break
print(sum_B - sum_A)