# from collections import deque

# N = int(input())                            # 0은 딸기만 1은 초코만 2는 바나나만. 딸-초-바 순으로 반복되어야함(0-1-2)
# info = list(map(int, input().split()))

# count = 0
# info2 = []             # 하나하나씩 왼쪽의 정보를 지우면서, 지우기전에 info2에 추가해놓을 예정. info2의 마지막 인덱스가 ~~ 라면 count+1 쓸수있을듯?
# info_q = deque(info)

# for i in info_q:
#     if info_q[0] == 0:
#         count += 1
#         info2.append(i)                 
#         info_q.popleft()

# for i in range(len(info)):
#     if i == 0:
#         if info[0] == 0:
#             count += 1
#         else:
#             continue
#     else:
#         if info[i] == 0 and info[i - 1] == 2:
#             count += 1
#         elif info[i] == 1 and info[i - 1] == 0:
#             count += 1
#         elif info[i] == 2 and info[i - 1] == 1 and info[i - 2] == 0:
#             count += 1
# print(count)

# from collections import deque

# N = int(input())                            # 0은 딸기만 1은 초코만 2는 바나나만. 딸-초-바 순으로 반복되어야함(0-1-2)
# info = list(map(int, input().split()))

# count = 0
# info2 = []             # 하나하나씩 왼쪽의 정보를 지우면서, 지우기전에 info2에 추가해놓을 예정. info2의 마지막 인덱스가 ~~ 라면 count+1 쓸수있을듯?
# info_q = deque(info)

# for i in range(N):
#     if info_q == deque([]):
#         break
#     while info2 == []:
#         if info_q[0] != 0:
#             info_q.popleft()
#         else:
#             info2.append(info_q[0])
#             info_q.popleft()
#     if info_q[0] == 0 and info2[-1] == 2:
#         info2.append(info_q[0])
#         info_q.popleft()
#     elif info_q[0] == 1 and info2[-1] == 0:
#         info2.append(info_q[0])
#         info_q.popleft()
#     elif info_q[0] == 2 and info2[-1] == 1:
#         info2.append(info_q[0])
#         info_q.popleft()
#     else:
# print(len(info2))

N = int(input())
info = list(map(int, input().split()))
# dic_info = {
#     0 : 0,
#     1 : 0,
#     2 : 0
# }


# for i in info:
#     if sum(dic_info.values()) == 0:
#         if i == 0:
#             dic_info[0] = 1
#     else:   
#         if i == 0 and dic_info[2] == dic_info[0]:
#             dic_info[0] = dic_info[0] + 1
#         if i == 1 and dic_info[0] == dic_info[1] + 1:
#             dic_info[1] = dic_info[1] + 1
#         if i == 2 and dic_info[0] == dic_info[1]:
#             dic_info[2] = dic_info[2] + 1
    
# print(sum(dic_info.values()))
milk = 0
count = 0
for i in range(len(info)):
    if info[i] == milk:
        count += 1                  # 너무쉬운문제를 헤맸다...... 반성하자
        milk +=1

    if milk == 3:
        milk = milk - 3

print(count)
