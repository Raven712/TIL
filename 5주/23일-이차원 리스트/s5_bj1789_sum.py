S = int(input())

num = 0
i_ = 0
for i in range(1, S):
    num += i
    i_ = i
    if num >= S:
        break
if S == 1 or S == 2:
    print(1)
else:
    if num == S:
        print(i_)
    else:
        print(i_ - 1)