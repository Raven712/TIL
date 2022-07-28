
N = int(input())
N_list = list(map(int,input().split()))

M = int(input())
M_list = list(map(int,input().split()))

N_dic = {}
for i in M_list:
    N_dic[i] = 0    # 정의하려고 한건데, ... 시간복잡도가 커져서 뻈음...

for i in range(len(N_list)):
    if N_list[i] in M_list:
        N_dic[N_list[i]] = N_dic[N_list[i]] + 1

for i in range(len(M_list)):
    print(N_dic[M_list[i]], end = ' ')    # 기존의 코드인데, 시간복잡도떄문에 일단 뻈다.

for i in M_list:
    print(N_dic.get(i), end = ' ')  # < 위와 아래는 같은것 아닌가 ??

# have = []
# for i in M_list:
#     have.append(N_dic[i])
# for i in have:
#     print(i, end = ' ')
# ans = []
# for i in M_list:
#     ans.append(N_dic[i])
# print(ans)


# 31초걸림