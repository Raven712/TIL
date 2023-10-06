#8 자리 정수주어질때 연속해서 같은숫자 없으면 1출력 있으면 길이제일긴거 출력
import sys
sys.stdin = open('seq.txt', 'r')

for i in range(3):
    num = input()   # 순회하려면 스트링이어야함
    max_ = 0
    max_set = set()
    for j in range(0, 8):
        if j == 0:                  #입력된 8자리 정수(지만 문자열인것)를 요소마다 순회하는데, 맨첫번쨰 요소는 일단 딕셔너리에 추가함 (인덱스 범위문제떄문에) <<< 딕셔너리를 쓰려고했으나 필요없어서 제거
            max_ = 1
            max_set.add(max_)
        else:
            if num[j] != num[j - 1]:            # 현재의 자리수와 이전자리수가 다를땐 기존의 최대값을 세트에 넣고, 최대값을 세는건 초기화시킴
                max_set.add(max_)
                max_ = 1
            else:
                max_ += 1
                max_set.add(max_)
    print(max(max_set))
            # if num[j] == num[j - 1]:
            #     if num[j] not in dic_num:
            #         dic_num[num[j]] = 1
            #     else:
            #         dic_num[num[j]] += 1
                