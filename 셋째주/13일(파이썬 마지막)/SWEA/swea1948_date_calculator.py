month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 :31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m, d, m1, d1 = map(int,input().split())
    #d1 > d 이면서 m1 > m인게 조건인듯 ??
    L = []    # 리스트에 월별 일 수를 집어넣고싶음.
    for i in range(1, 13):   #월은 12까지 있으니 레인지 13까지 해야함.
        L.append(month[i])    # 리스트에 month의 월별 키 값을 (날짜 수) 집어넣음.    ** 여기서 append를 해서 리스트의 0번 요소부터 1월이 시작됨 .... 헷갈리게 됐음 이것때문에 !! 더좋은방법 있을까 ??
    for i in range(1, 12):   # 우리는 날짜 차이를 계산해야하니 월별 일수 누적치를 리스트에 등록하는게 목적임. (2월이면 59일 n월이면 n일.. 이래야 사칙연산이 편해지니)
        L[i] = L[i-1] + L[i]
            # 한참뒤에 계산하면서 알았는데, 리스트 0번부터 31이라서 1월 2일이 2로 계산돼야하는데 33으로 계산되는 상황이 나타남.. 그래서, 밑에 L1을 추가로 만듬..

    L1 = []
    for i in range(0, 13):
        if i == 0:
            L1.append(0)
        else:
            L1.append(L[i-1])        # L1은 13개의 인덱스로 이뤄져있고 0번은 0부터 시작함. 이래야 계산하기 편함 ..

    cal = L1[m1-1] - L1[m-1] + d1 - d + 1      # 여기 +1이 왜 붙어야 정답이 되는건진 모르겠다
    print(f'#{test_case} {cal}')