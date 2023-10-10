N = int(input())

li_ = list(map(int, input().split()))

M = max(li_)

for i in range(len(li_)):
    New = (li_[i] / M) * 100
    li_[i] = New

def avg(x):                 # 파이썬에는 평균구하는 함수가 없는듯?
    avg_ = sum(x) / len(x)
    return avg_

print(avg(li_))