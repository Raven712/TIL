# N = 학생수. 그리고 N명의 점수가 주어짐. 점수는 0~100.
#그래서 평균넘는사람은 몇퍼? 를 출력.

C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    sum_ = 0    # 평균구하려면 합필요
    overmean = [] # 평균넘는사람들의 리스트. 이 리스트 길이에 전체길이를 나눌 예정
    for j in range(1, len(N)):
        sum_ += N[j]
    mean = sum_ / (len(N) - 1)
    
    for j in range(1, len(N)):
        if N[j] > mean:
            overmean.append(N[j])
    ans = len(overmean) / (len(N) - 1)
    # print(f'{round(ans * 100,3)}%')         # round 는 자기맘대로 중간에서 끊어버림
    print('%.3f' %(ans * 100) + '%')