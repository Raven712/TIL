# 1회 : 100명출전 21명만 1등 1명 2등 2명.. 6등 6명 상금 각자다름. 500 300 200 50 30 10 (a등하면 얼마받을까)

# 2회 : 64명중 31명만 1등 1명 2등 2명 5등 2^5-1 명 512 256 128 64 32(상금) (b등하면 얼마받을까)

T = int(input()) 
dic_1 = {
    1 : 5000000,
    2 : 3000000,
    3 : 2000000,
    4 : 500000,
    5 : 300000,
    6 : 100000
}
dic_2 = {
    1 : 5120000,
    2 : 2560000,
    3 : 1280000,
    4 : 640000,
    5 : 320000
}

prize_a = 0
prize_b = 0

for i in range(T):
    a, b = map(int, input().split())
    if a == 1:
        prize_a = dic_1[1]
    elif 3 >= a >= 2:
        prize_a = dic_1[2]
    elif 6 >= a >= 4:
        prize_a = dic_1[3]
    elif 10 >= a >= 7:
        prize_a = dic_1[4]
    elif 15 >= a >= 11:
        prize_a = dic_1[5]
    elif 21 >= a >= 16:
        prize_a = dic_1[6]
                                                            # 이건 좀 아니지않나
    if b == 1:
        prize_b = dic_2[1]
    elif 3 >= b >= 2:
        prize_b = dic_2[2]
    elif 7 >= b >= 4:
        prize_b = dic_2[3]
    elif 15 >= b >= 8:
        prize_b = dic_2[4]
    elif 31 >= b >= 16:
        prize_b = dic_2[5]
    
    print(prize_a + prize_b)
    prize_a = 0
    prize_b = 0
