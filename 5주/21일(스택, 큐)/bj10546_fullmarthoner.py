N = int(input())
name = list(input() for i in range(N))
name2 = list(input() for i in range(N-1))
dic_name = {}                     # 리스트를 쓰니까 시간초과되는 문제다.  /// 딕셔너리도 for문을 막 쓰니까 시간초과.. while써도 시간초과
dic_name2 = {}
for i in range(N):
    if name[i] not in dic_name:
        dic_name[name[i]] = 1
    else:
        dic_name[name[i]] = dic_name[name[i]] + 1

for j in range(N-1):
    cnt = dic_name[name2[i]]
    dic_name[name2[i]] = cnt - 1

for i in dic_name:
    if dic_name[i] == 1:
        print(i)
        break
    # if i not in dic_name2 or dic_name[i] != dic_name2[i]:
    #     print(i)
    #     break
    # elif dic_name[i] != dic_name2[i]:
    #     print(dic_name[i])
    #     break

# list_name = []  #참가자
# list_name2 = []     #중에 진짜 뛴사람
# for i in range(N):
#     name = input()
#     list_name.append(name)

# for j in range(N - 1):
#     name2 = input()
#     list_name2.append(name2)

# # list_name = sorted(list_name)     #정렬이 필요없을것같아서 뻄
# # list_name2 = sorted(list_name2)  # 두개를 정렬후 끝부분에서부터 비교후 같다면 마지막을 빼고 .. 1에는 있는데 2에는 없는게 나올때까지 반복

# while list_name[-1] in list_name2:
#     list_name.pop()
#     if len(list_name) == 1:
#         print(list_name[0])
#         break
# if list_name == []:
#     pass
# else:
#     print(list_name[-1])

