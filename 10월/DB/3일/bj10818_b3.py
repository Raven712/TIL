N = int(input())

list_ = list(map(int, input().split()))
Max_ = -1000000
Min_ = 1000000
for i in list_:
    if i >= Max_:
        Max_ = i
    if i <= Min_:
        Min_ = i
print(Min_, Max_)