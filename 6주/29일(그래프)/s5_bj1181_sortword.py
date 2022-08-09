#알파벳소문자단어가 N개만큼 입력. 길이 짧은순 -> 같다면 사전순 출력.
import sys
sys.stdin = open('단어.txt', 'r')
from collections import deque

N= int(input())
list_ = []
for i in range(N):
    word = input()
    list_.append(word)

list_ = list(set(list_))
list_.sort()

list_.sort(key = lambda x : len(x)) # 핵심 !!!!!!!!!

for i in list_:
    print(i)








# list_len = []
# for i in list_:
#     list_len.append(len(i))

# list_len.sort()
# deque_len = deque(list_len)


# list_2 = []
# for i in range(N):
#     if len(list_[i]) == min(deque_len):
#         list_2.append(list_[i])             # 이렇게하니까 list_ 가 길이순정렬이 안돼서 제대로 작동이 안된다 . 
#         deque_len.popleft()
