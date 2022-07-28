# first = list(input().split())
# second = list(input().split())                                        # 리스트를 만들어도 인덱스 개수조절문제가 어렵다.
                                                                        #
# third = list(input().split())
# fourth = list(input().split())  # 여기서부터 틀렸다. 한줄로 입력임
# fifth = list(input().split())

# vert = []
# length = []
# length.append(len(first))
# length.append(len(second))
# length.append(len(third))
# length.append(len(fourth))
# length.append(len(fifth)) ## 손으로 노가다한건, for문을 쓰면 복잡도가 오르는데 어펜드함수만 쓰면 복잡도가 상수라서 안써봤음. 

# max_ = max(length) # 아래 for문에서 범위에러가 안나게, 세로로 탐색하는 범위를 유효한 최대범위까지만 .. ?하게... 하려면 min을 써야하는데,,, min을 쓰면 다 넣을수가 없음 ..

# for i in max_:
#     vert.append(first[i])
#     vert.append(second[i])


# first = input()
# second = input()
# third = input()
# fourth = input()
# fifth = input()
# vert = []

# for i in range(15):
#     if first == []:
#         conitnue
#     else:
#         vert.append(first[i])
#     if second == []:
#         continue
#     else:        
#         vert.append(second[i])
#     if third == []:
#         continue                  #아무리봐도 망했다
#     else:    
#         vert.append(third[i])
#     if fourth == []:
#         continue
#     else:
#         vert.append(fourth[i])
#     if fifth == []:
#         continue
#     else:    
#         vert.append(fifth[i])

# print(vert)
length = []
list_ = []
for i in range(5):
    word = input()
    list_.append(word)    # 입력된 단어를 저장한 리스트를 만듬. 
    length.append(len(word))

max_ = max(length)    
vert = []
word2 = ''
for i in range(max_):
    for j in range(5):
        if i < length[j]:
            word2 += list_[j][i]
print(word2)