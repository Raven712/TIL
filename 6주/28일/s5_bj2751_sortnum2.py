import sys
input = sys.stdin.readline

N= int(input())
list_ = []
for i in range(N):
    a = int(input())
    list_.append(a)

list_ = sorted(list_)

for i in list_:
    print(i)
