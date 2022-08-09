# 나이 오름차순, 나이같으면 먼저가입한사람 나오게 출력
import sys
sys.stdin = open('나이.txt','r')

N = int(input())

list_ = []
list_name = []
for i in range(N):
    age, name = input().split()
    list_.append([age, name])
    list_name.append(name)

list_.sort(key = lambda x : x[0])   ## 핵심 !!  
print(list_) 