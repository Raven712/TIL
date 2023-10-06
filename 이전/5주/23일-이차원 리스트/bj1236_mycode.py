#N, M 행렬. 그냥 대각선에 경비가 있으면 되는듯 << ㄴㄴ

# 경비가 있으면 경비가있는 행,열은 모두 경비가 필요없어짐
# X[i][j] == 'X' 일떄... X[i][0~M] 과 X[0~N][j] 는 경비필요없는것... 이걸 O로 표시하자
# 그렇게 되면 X에서 . 인것들의 갯수를 다 더하면 된다

N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(list(input()))

count_X = 0 #필요 경비원수

for i in range(N):
    for j in range(M):
        if X[i][j] == '.':
            for k in range(M):
                if X[i][k] == 'X':
                    X[i][j] = 'O'                       ## 3중 for문을 썼다. 심지어 틀렸다. 테스트케이스는 맞는데?
            for l in range(N):
                if X[l][j] == 'X':
                    X[i][j] = 'O'
for i in X:
    # if '.' in i:
    #     count_X += 1           
    for j in i:                  # 여기를 다시 이중 for문을 써서 i안의 j들로 바꿨다. 그러니까... 또틀렸다
        if j == '.':
            count_X += 1
print(count_X)
