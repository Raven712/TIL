#N, M 행렬. 그냥 대각선에 경비가 있으면 되는듯 << ㄴㄴ

# 경비가 있으면 경비가있는 행,열은 모두 경비가 필요없어짐
# X[i][j] == 'X' 일떄... X[i][0~M] 과 X[0~N][j] 는 경비필요없는것... 이걸 O로 표시하자
# 그렇게 되면 X에서 . 인것들의 갯수를 다 더하면 된다

# N, M = map(int, input().split())
# X = []
# for i in range(N):
#     X.append(list(input()))

# count_X = 0 #필요 경비원수

# for i in range(N):
#     for j in range(M):
#         if X[i][j] == '.':
#             for k in range(M):
#                 if X[i][k] == 'X':
#                     X[i][j] = 'O'            
#             for l in range(N):
#                 if X[l][j] == 'X':
#                     X[i][j] = 'O'
# for i in X:
#     for j in i:
#         if j == '.':
#             count_X += 1
# print(count_X)

N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(list(input()))

count_X = 0 #필요 경비원수

row = [0] * N               #행과 열을 따로분석하는게 핵심이었음
col = [0] * M

for i in range(N):
    for j in range(M):
        if X[i][j] == 'X':
            row[i] += 1
            col[j] += 1

row_count = 0                  
col_count = 0

for i in row:
    if i == 0:          #경비가 없는 열의 개수를 체크
        row_count += 1
for i in col:           # '' 행개수체크
    if i == 0:
        col_count += 1

print(max(row_count, col_count))

    