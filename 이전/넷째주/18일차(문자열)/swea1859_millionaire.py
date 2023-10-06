import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    buy = list(map(int,input().split()))
    margin = 0
    pay = 0
    list_margin = []
    keep = []
    max_ = max(buy)
    top = buy.index(max_)           # 리스트의 특정요소 위치찾는법! 

    # for i in range(N - 1):
        # if buy[i + 1] < buy[i]:              ## 여기서 틀렸다. i번째 값이 4300, 그다음값이 3900, 그다음 4700, 다음 8400이면 4300도 사야하는데, 4300이 3900보다 크니까 안사고 넘어감 !!!!
        #     margin = buy[i] * len(keep) - pay               ## 즉 우리는 끝나기전의 최대값까진 전부다 사놔야함 !!!!!!!!!!! 
        #     list_margin.append(margin)
        #     margin = 0
        #     pay = 0
        #     keep = []
        # else:
        #     keep.append(buy[i])
        #     pay += buy[i]

    # margin = buy[-1] * len(keep) - pay
    # list_margin.append(margin)

    # total = sum(list_margin)
    for i in range(N - 1):
        if i < top:
            keep.append(buy[i])
            pay += buy[i]
        elif i == top:
            margin = max_ * len(keep) - pay
            list_margin.append(margin)
            margin = 0
            pay = 0
            keep = []
        else:               # 위 과정이 끝나면 top 이후부터 다시 그영역의 최대값 찾고 다사고 최대값일때 팔고를 끝날때까지 반복해야하는데 .. ????
            for j in range(i + 1, N - 1)   
        
    print(f'#{test_case} {total}')

    #어디가 틀린지 모르겠음.