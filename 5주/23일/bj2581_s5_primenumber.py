# M N주어짐. M이상 N이하 중 소수인걸 모두골라, 그 합과 최소값 찾기.
# 소수는 //로 찾으면 되는듯  ?  

M = int(input())
N = int(input())
min_ = []
sum_ = 0
for i in range(M, N + 1):
    for j in range(2, i + 1):
        if j == i:
            min_.append(i)
            sum_ += i
            break
        if i // j == i / j:
            break
if min_ != []:        
    print(sum_)
    print(min_[0])
else:
    print(-1)