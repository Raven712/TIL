sum_ = 0
list_ = []
for i in range(5):
    n = int(input())
    sum_ += n
    list_.append(n)
E = sum_ / 5 #평균
print(int(E)) #자연수 조건떄문에 int 씀

list_.sort()
print(list_[2]) #중앙값