N = int(input())
dic_name = {}                     # 리스트를 쓰니까 시간초과되는 문제다. 
dic_name2 = {}
for i in range(N):
    name = input()
    if name not in dic_name:
        dic_name[name] = 1
    else:
        dic_name[name] = dic_name[name] + 1

print(dic_name)