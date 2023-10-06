# 평균과 최빈값 구하기. 10개 자연수주어짐   ///// 딕셔너리에 max쓰니까 키값이 큰걸 출력해버림
sum_ = 0
dic_num = {}
for i in range(10):
    n = int(input())
    sum_ += n
    if n not in dic_num:
        dic_num[n] = 1
    else:
        dic_num[n] += 1

print(int(sum_ / 10))

print(max(dic_num, key = dic_num.get))