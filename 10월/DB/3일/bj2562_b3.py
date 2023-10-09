list_ = []
Max_ = 0
Max_num = 0

for i in range(1, 10):
    K = int(input())
    list_.append(K)
    if list_[-1] > Max_:
        Max_ = list_[-1]
        Max_num = i

print(Max_)
print(Max_num)

