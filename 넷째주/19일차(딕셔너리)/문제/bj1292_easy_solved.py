# lim_ = 0
# for i in range(100):
#     if i * (i+1) /2 > 1000:
#         lim_ = i
#         break
# list_ = []
# for i in range(1, lim_ + 1):
#     list_.append(int(i * (i + 1) / 2))   # int를 안하면 float형으로 됨. 이유는 모르겠음 나누기해서그런가 ??


# A, B = map(int, input().split())

# for i in range(list_):
#     if A < list[i]

A, B = map(int, input().split())

# sum_A = []
# for i in range(A):
#     sum_A.append(i ** 2)            

# sumA = sum(sum_A)

# for i in range(B + 1):
# if A <
loc_low = 0
loc_high = 0
sub2 = 0 #A
for i in range(1, 46):          #위에서 확인한결과 최대치 1000은 45~46이 출력될때 끝남
    if A <= i * (i + 1) / 2:      # 자릿수는 1,3,6,10 즉 n까지의 합과같음. 예를들어 9번쨰자리에 A가 있다칠때 9는 6,10 사이이므로, 그 사이에는 4가 출력되고 있음... 
        loc_low = i * (i - 1) / 2      #loc_low는 A보다 1작은 수의 합.. 즉 A의 위치는 loc_low에서 몇개정도 더 나가져있는 상태
        loc_high = i * (i + 1) / 2
        sub2 = i - 1
        break
sum_1 = 0
for i in range(1, sub2 - 1):
    sum_1 += i ** 2

sub = sum_1 + (sub2 * (A - loc_low))

print(sub)

#필요한것 : A는 몇이 출력되고 있는가 : A< i(i+1)/2 일때 , A에선 io이 출r i-1력되고있음. i-1이 출력되는건 
#i -2 까지의 제곱합을 구하고, 거기에 (A-1) - (i-2 제곱합이 끝나는 위치) 즉 (A-1) - (i-2)(i-1)/2)에다가 * (i-1) 을 하면, A하나앞까지의 숫자합을 구할수있음. (이걸 나중에 빼야함.)
#B는, B<= n(n+1)/2 일떄 B에선 n-1이 출력되는중


