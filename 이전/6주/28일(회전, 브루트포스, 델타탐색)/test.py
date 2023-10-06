N = int(input())
list_ = []
for i in range(N):
    x = int(input()) #주어지는 값들의 ~~ 출력하기.
    list_.append(x)
sum_ = sum(list_)
list_ = sorted(list_)

print('{:.0f}'.format(sum_ / N))# 1
print(sum_/N)

    