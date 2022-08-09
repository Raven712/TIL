N = int(input())

list_ = []
for i in str(N):
    list_.append(i)

list_.sort()
list_ = list_[::-1]
for i in list_:
    print(i, end = '')