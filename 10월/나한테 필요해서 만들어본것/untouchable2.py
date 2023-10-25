# 총 비용에만 초점을 두고, 특정 골드를 가지고 n번의 시행을 했을때 평균비용이 얼마가 나오는지 측정해보자

# 투입될 골드, 불가침 깡통가격, 추출기 가격, 힘정값, 시작레벨이 입력된다
import random
from collections import Counter
gold, item, ext, power, lev = map(int, input().split())
extract = (ext + item) / 19
gold_origin = gold
lev_origin = lev

# 2렙업 1퍼, 1렙업 38퍼, 유지 31퍼, 하락 30퍼
weight = [0.01, 0.38, 0.31, 0.3]

N = int(input()) # 시행 횟수
mean = []  # 평균 비용, 매 시행에 들어간 골드 합 / N을 할 예정
success = 0
fail = 0        # 성공과 실패의 횟수
fail_lev = []
for i in range(N):
    # cnt는 트라이횟수 cost는 총비용 list_는 매 시도 기록을 담아놓는곳 
    gold = gold_origin
    lev = lev_origin
    cnt = 0
    cost = 0
    list_ = []
    while 0 < lev < 70 and gold >= 0:
        if 1 <= lev <= 30:
            gold = gold - 20000 - extract - power
            cost += 20000 + extract + power
            cnt += 1
            temp = random.choices([2, 1, 0, -1], weight)
            list_.append(temp[0])            
            lev = lev + temp[0]
            
        elif 31 <= lev <= 50:
            gold = gold - 50000 - (2 * extract) - (2 * power)
            cost += 50000 + (2 * extract) + (2 * power)
            cnt += 1
            temp = random.choices([2, 1, 0, -1], weight)
            list_.append(temp[0])           
            lev = lev + temp[0]

        elif 51 <= lev <= 60:
            gold = gold - 300000 - (8 * extract) - (5 * power)
            cost += 300000 + (8 * extract) + (5 * power)
            cnt += 1
            temp = random.choices([2, 1, 0, -1], weight)
            list_.append(temp[0])            
            lev = lev + temp[0]

        elif 61 <= lev < 70:
            gold = gold - 1300000 - (30 * extract) - (10 * power)
            cost += 1300000 + (30 * extract) + (10 * power) 
            cnt += 1
            temp = random.choices([2, 1, 0, -1], weight)
            list_.append(temp[0])            
            lev = lev + temp[0]
    mean.append(cost) # 현재 mean은 70작 트라이가 끝난 후에 들어간 비용이 모두 들어간 리스트
    if lev >= 70:
        success += 1
    else:
        fail += 1
        fail_lev.append(lev)

mean_value = 0

min_ = min(mean) # N번의 시행 후 최소로 찍힌 값
max_ = max(mean) # N번의 시행 후 최대로 찍힌 값
for i in range(N):
    mean_value += mean[i]

mean_value = mean_value / N
print(f"평균 비용은 {round(mean_value)}, 최소 비용은 {round(min_)}, 최대 비용은 {round(max_)}, 성공 횟수는 {success}, 돈이 바닥난 횟수는{fail}, 실패했을때의 레벨은 {fail_lev} 입니다")
# print(lev, cnt, cost, Counter(list_))