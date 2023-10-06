# 1~100정수 적어내기. 같은수 적은사람 없으면 그만큼 점수획득, 있으면 컨티뉴 // 3회시행.
# 특정 열의 값이 다른행의 특정 열 값과 같으면 0점을 얻음...
# 플레이어는 입력되는 값만큼 생기는데 어떻게 점수를 누적시킬까 

N = int(input())  #참가자 수

point_list = []
count_dic = {}     #플레이어별 점수딕셔너리로 사용할 예정 

for i in range(N):
    card = list(map(int, input().split()))
    point_list.append(card)
    count_dic[i] = 0        

round1_list = [] #라운드별 점수모음
round2_list = []
round3_list = []

for i in point_list:
    round1_list.append(i[0])
    round2_list.append(i[1])
    round3_list.append(i[2])

point_dic = {}          # 딕셔너리를 만들어서 처음 적어내는값은 딕셔너리에 등록시키고,
                         # 딕셔너리에 등록되있는 값을 적어냈다면 count_dic에 점수를 0점 받게할 예정

for i in range(N):
    if round1_list[i] not in point_dic:                                   #적어낸 점수가 적어낸 점수딕셔너리에 없다면 
        point_dic[round1_list[i]] = 1                                       # 점수딕셔너리에 적어낸 점수를 등록하고  
    else:
        point_dic[round1_list[i]] = 0
for i in range(N):
    if point_dic[round1_list[i]] == 0:
        count_dic[i] += 0
    else:
        count_dic[i] += round1_list[i]

point_dic = {}

for i in range(N):
    if round2_list[i] not in point_dic:                                   #적어낸 점수가 적어낸 점수딕셔너리에 없다면 
        point_dic[round2_list[i]] = 1                                       # 점수딕셔너리에 적어낸 점수를 등록하고  
    else:
        point_dic[round2_list[i]] = 0
for i in range(N):
    if point_dic[round2_list[i]] == 0:
        count_dic[i] += 0
    else:
        count_dic[i] += round2_list[i]
                  
point_dic = {}

for i in range(N):
    if round3_list[i] not in point_dic:                                   #적어낸 점수가 적어낸 점수딕셔너리에 없다면 
        point_dic[round3_list[i]] = 1                                       # 점수딕셔너리에 적어낸 점수를 등록하고  
    else:
        point_dic[round3_list[i]] = 0
for i in range(N):
    if point_dic[round3_list[i]] == 0:
        count_dic[i] += 0
    else:
        count_dic[i] += round3_list[i]
                               
  
for i in range(N):
    print(count_dic[i])