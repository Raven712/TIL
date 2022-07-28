N, M = map(int,(input().split()))

d_dic = {}
bo_dic = {}

for i in range(N):
    d = input()   # if 문을 추가로 쓸게없는게, 겹치는 이름이 안나타난다고 한다.
    d_dic[d] = 1
    
for i in range(M):
    bo = input()
    bo_dic[bo] = 1
    
job_dic = {}
for i in d_dic:
    if i in bo_dic:
        job_dic[i] = 1

job_list = []
for i in job_dic:
    job_list.append(i)

job_list = sorted(job_list)

print(len(job_dic))
for i in job_list:
    print(i)
