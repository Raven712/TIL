# 투입될 골드, 불가침 깡통가격, 추출기 가격, 힘정값, 시작레벨이 입력된다
import random
from collections import Counter
gold, item, ext, power, lev = map(int, input().split())

extract = (ext + item) / 19
# 2렙업 1퍼, 1렙업 38퍼, 유지 31퍼, 하락 30퍼
weight = [0.01, 0.38, 0.31, 0.3]

# cnt는 트라이횟수 cost는 총비용 list_는 매 시도 기록을 담아놓는곳
cnt = 0
cost = 0
cnt_power = 0
cnt_ext = 0
cnt_gold = 0
list_ = []
list_30 = []
list_50 = []
list_60 = []
list_70 = []
while 0 < lev < 70 and gold >= 0:
    if 1 <= lev <= 30:
        gold = gold - 20000 - extract - power
        cost += 20000 + extract + power
        cnt_power += 1
        cnt_ext += 1
        cnt_gold += 20000
        cnt += 1
        temp = random.choices([2, 1, 0, -1], weight)
        list_.append(temp[0])
        list_30.append(temp[0])
        lev = lev + temp[0]
        
    elif 31 <= lev <= 50:
        gold = gold - 50000 - (2 * extract) - (2 * power)
        cost += 50000 + (2 * extract) + (2 * power)
        cnt += 1
        cnt_power += 2
        cnt_ext += 2
        cnt_gold += 50000
        temp = random.choices([2, 1, 0, -1], weight)
        list_.append(temp[0])
        list_50.append(temp[0])
        lev = lev + temp[0]

    elif 51 <= lev <= 60:
        gold = gold - 300000 - (8 * extract) - (5 * power)
        cost += 300000 + (8 * extract) + (5 * power)
        cnt += 1
        cnt_power += 5
        cnt_ext += 8
        cnt_gold += 300000
        temp = random.choices([2, 1, 0, -1], weight)
        list_.append(temp[0])
        list_60.append(temp[0])
        lev = lev + temp[0]

    elif 61 <= lev < 70:
        gold = gold - 1300000 - (30 * extract) - (10 * power)
        cost += 1300000 + (30 * extract) + (10 * power) 
        cnt += 1
        cnt_power += 10
        cnt_ext += 30
        cnt_gold += 1300000
        temp = random.choices([2, 1, 0, -1], weight)
        list_.append(temp[0])
        list_70.append(temp[0])
        lev = lev + temp[0]

print(lev, cnt, round(cost), cnt_power, cnt_ext, cnt_gold, Counter(list_), len(list_60), len(list_70))