N = int(input())
List_ = []     # 아래 for문에서 키몸무게를 입력하고, 그걸 리스트로 만든뒤 다시 리스트에 넣음 .. 이중 리스트가 됐는데, 더 밑의 다른 for문에서 비교를 한번에 하려고 그랬음
for i in range(1, N + 1):
    build = list(map(int, input().split()))
    List_.append(build) 
    
    #위의 작업으로 키, 몸무게가 요소로 있는 리스트를 List_에 넣었음

List2 = [1] * N     # 등수를 넣기위한 리스트를 미리 만듬

for i in range(N):
    for j in range(N):
        if List_[i][0] < List_[j][0] and List_[i][1] < List_[j][1]:     # i번째 사람의 키, 몸무게에 대해서, j번째 사람의 키 몸무게를 비교하려고 이중for문을 사용했는데, 
            List2[i] += 1                                                  # i번째 사람이랑 j번쨰사람을 비교해놓고 j번쨰 사람이랑 i번쨰 사람이랑 비교할 필요가 없으니,
                                                                                # 효율적으로 했다면 for j문에선 range(i + 1, N) 을 해도 됐을것같음
for i in List2:
    print(i, end = ' ')     #리스트상태를 그냥 숫자로 출력